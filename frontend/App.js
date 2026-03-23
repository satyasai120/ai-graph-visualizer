import React, { useState } from "react";
import GraphView from "./GraphView";

function App() {
  const [query, setQuery] = useState("");
  const [graphData, setGraphData] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateGraph = () => {
    fetch("http://127.0.0.1:5001/generate-graph", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
    
      body: JSON.stringify({ query })
    })
      .then((res) => res.json())
      .then((data) => setGraphData(data))
      .catch((err) => console.error(err));
  };


  return (
    <div style={{ padding: "20px", fontFamily: "Arial", textAlign: "center" }}>
      <h2>AI Graph Generator</h2>

      <input
        type="text"
        placeholder="Example: Order -> Payment -> Delivery"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{ width: "350px", marginRight: "10px" }}
      />

      <button onClick={generateGraph}>Generate Graph</button>
      <button style={{
        padding: "8px 16px",
        background: "blue",
        color: "white",
        border: "none",
        cursor: "pointer"
      }}> Generate </button>

      {graphData && <GraphView data={graphData} />}
    </div>
  );
}

export default App;
