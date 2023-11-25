import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def girvan_newman_step(graph, pos, ax):
    """
    Perform one step of the Girvan-Newman algorithm and update the plot.
    """
    # Calculate edge betweenness centrality
    betweenness = nx.edge_betweenness_centrality(graph)

    # Find the edge with the highest betweenness centrality
    max_edge = max(betweenness, key=betweenness.get)

    # Remove the edge with the highest betweenness centrality
    graph.remove_edge(*max_edge)

    # Draw the updated graph
    ax.clear()
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10)
    plt.draw()

def on_button_click(event):
    girvan_newman_step(G, pos, ax)

# Create a graph
G = nx.karate_club_graph()
pos = nx.spring_layout(G)

# Create a plot
fig, ax = plt.subplots()
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10)

# Create a button
ax_button = plt.axes([0.81, 0.01, 0.1, 0.05])  # [x, y, width, height]
button = Button(ax_button, 'Next Step', color='lightgoldenrodyellow', hovercolor='0.975')

# Attach the button callback function
button.on_clicked(on_button_click)

# Show the plot
plt.show()
