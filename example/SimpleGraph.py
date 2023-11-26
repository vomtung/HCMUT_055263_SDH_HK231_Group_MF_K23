import networkx as nx
import matplotlib.pyplot as plt

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])

# Calculate edge betweenness centrality
edge_betweenness = nx.edge_betweenness_centrality(G)

# Print edge betweenness for each edge
for edge, betweenness in edge_betweenness.items():
    print(f"Edge {edge}: {betweenness}")

# Optionally, you can visualize the graph with edge betweenness values


pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{betweenness:.2f}' for (u, v), betweenness in edge_betweenness.items()})
plt.show()
