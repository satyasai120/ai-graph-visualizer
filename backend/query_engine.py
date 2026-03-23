from collections import defaultdict

class QueryEngine:
    def __init__(self, graph):
        self.graph = graph

    def get_unbilled_orders(self):
        result = []
        for node in self.graph.nodes:
            if self.graph.nodes[node]['type'] == 'order':
                deliveries = list(self.graph.successors(node))
                billed = any(
                    list(self.graph.successors(d)) for d in deliveries
                )
                if not billed:
                    result.append(node)
        return result

    def trace_order_flow(self, order_id):
        node = f"order_{order_id}"
        flow = []

        for d in self.graph.successors(node):
            flow.append(d)
            for i in self.graph.successors(d):
                flow.append(i)
                for p in self.graph.successors(i):
                    flow.append(p)

        return flow

    def top_products(self):
        product_count = defaultdict(int)

        for u, v, data in self.graph.edges(data=True):
            if data.get("relation") == "CONTAINS_PRODUCT":
                product_count[v] += 1

        return sorted(product_count.items(), key=lambda x: x[1], reverse=True)[:5]