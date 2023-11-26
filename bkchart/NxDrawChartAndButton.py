import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Create a graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5), (4, 5)])

# Create a plot
fig, ax = plt.subplots()
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10)

# Define the button callback function
def on_button_click(event):
    # Modify the graph (add an edge, for example)
    G.add_edge(1, 5)

    # Clear the current plot
    ax.clear()

    # Redraw the updated graph
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10)

    # Redraw the buttons
    plt.draw()

# Create a button
ax_button = plt.axes([0.81, 0.01, 0.1, 0.05])  # [x, y, width, height]
button = Button(ax_button, 'Add Edge', color='lightgoldenrodyellow', hovercolor='0.975')

# Attach the button callback function
button.on_clicked(on_button_click)

# Show the plot
plt.show()
