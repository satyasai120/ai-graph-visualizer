from fastapi import FastAPI
from graph_builder import GraphBuilder
from query_engine import QueryEngine
from llm import parse_query

app = FastAPI()

builder = GraphBuilder()
builder.load_data(
    "../data/orders.csv",
    "../data/deliveries.csv",
    "../data/invoices.csv",
    "../data/payments.csv"
)

graph = builder.build_graph()
engine = QueryEngine(graph)

@app.get("/query")
def query(q: str):
    parsed = parse_query(q)
    intent = parsed["intent"]
    params = parsed.get("parameters", {})

    if intent == "unbilled_orders":
        return {"result": engine.get_unbilled_orders()}

    elif intent == "trace_order":
        return {
            "result": engine.trace_order_flow(params.get("order_id"))
        }

    elif intent == "top_products":
        return {"result": engine.top_products()}

    return {"error": "Unknown query"}