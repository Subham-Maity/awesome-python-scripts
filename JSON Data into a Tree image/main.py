import json
from graphviz import Digraph

# Load JSON data from file
with open('package-lock.json', 'r') as f:
    data = json.load(f)

# Create a new directed graph
dot = Digraph()

# Define a recursive function to add nodes and edges to the graph
def add_nodes_edges(data, parent=None):
    if isinstance(data, dict):
        for key, value in data.items():
            dot.node(key)
            if parent:
                dot.edge(parent, key)
            add_nodes_edges(value, key)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            node_id = f'{parent}_{i}'
            dot.node(node_id, str(item))
            dot.edge(parent, node_id)
            add_nodes_edges(item, node_id)

# Call the recursive function on the JSON data
add_nodes_edges(data)

# Save the generated image to a file
dot.render('tree.gv', view=True)