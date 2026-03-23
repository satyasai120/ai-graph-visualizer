from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def get_graph():
    return "Backend Running Successfully"

@app.route("/generate-graph", methods=["POST"])
def generate_graph():
    return jsonify({
        "nodes": [
            {"id": "A"},
            {"id": "B"},
            {"id": "C"}
        ],
        "edges": [
            {"source": "A", "target": "B"},
            {"source": "B", "target": "C"}
        ]
    })

if __name__ == "__main__":
    app.run(port=5001, debug=True)
