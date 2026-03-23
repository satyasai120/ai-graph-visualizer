class QueryEngine:
    def __init__(self, graph):
        self.graph = graph

    def get_unbilled_orders(self):
        result = []
        for node in self.graph.nodes:
            if self.graph.nodes[node]['type'] == 'order':
                deliveries = list(self.graph.successors(node))
                billed = False

                for d in deliveries:
                    invoices = list(self.graph.successors(d))
                    if invoices:
                        billed = True

                if not billed:
                    result.append(node)

        return result

    def trace_order_flow(self, order_id):
        flow = []
        node = f"order_{order_id}"

        for d in self.graph.successors(node):
            flow.append(d)
            for i in self.graph.successors(d):
                flow.append(i)
                for p in self.graph.successors(i):
                    flow.append(p)

        return flow