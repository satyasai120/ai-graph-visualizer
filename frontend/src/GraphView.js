import React, { useEffect, useRef } from "react";
import cytoscape from "cytoscape";

function GraphView() {
  const cyRef = useRef(null);

  useEffect(() => {
    const cy = cytoscape({
      container: cyRef.current,

      elements: [
        { data: { id: "1" } },
        { data: { id: "2" } },
        { data: { id: "3" } },
        { data: { source: "1", target: "2" } },
        { data: { source: "2", target: "3" } }
      ],

      style: [
        {
          selector: "node",
          style: {
            label: "data(id)",
            "background-color": "green",
            color: "white"
          }
        },
        {
          selector: "edge",
          style: {
            width: 3,
            "line-color": "black"
          }
        }
      ],

      layout: { name: "grid" }
    });

    return () => cy.destroy();
  }, []);

  return (
    <div
      ref={cyRef}
      style={{ width: "100%", height: "600px", border: "2px solid black" }}
    />
  );
}

export default GraphView;