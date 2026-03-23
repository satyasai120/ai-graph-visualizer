import pandas as pd
import networkx as nx

class GraphBuilder:
    def __init__(self):
        self.graph = nx.DiGraph()

    def load_data(self, orders, deliveries, invoices, payments):
        self.orders = pd.read_csv(orders)
        self.deliveries = pd.read_csv(deliveries)
        self.invoices = pd.read_csv(invoices)
        self.payments = pd.read_csv(payments)

    def build_graph(self):
        for _, row in self.orders.iterrows():
            self.graph.add_node(f"order_{row['order_id']}", type="order", **row.to_dict())

        for _, row in self.deliveries.iterrows():
            self.graph.add_node(f"delivery_{row['delivery_id']}", type="delivery", **row.to_dict())
            self.graph.add_edge(
                f"order_{row['order_id']}",
                f"delivery_{row['delivery_id']}",
                relation="DELIVERED_AS"
            )

        for _, row in self.invoices.iterrows():
            self.graph.add_node(f"invoice_{row['invoice_id']}", type="invoice", **row.to_dict())
            self.graph.add_edge(
                f"delivery_{row['delivery_id']}",
                f"invoice_{row['invoice_id']}",
                relation="BILLED_AS"
            )

        for _, row in self.payments.iterrows():
            self.graph.add_node(f"payment_{row['payment_id']}", type="payment", **row.to_dict())
            self.graph.add_edge(
                f"invoice_{row['invoice_id']}",
                f"payment_{row['payment_id']}",
                relation="PAID_BY"
            )

        return self.graph