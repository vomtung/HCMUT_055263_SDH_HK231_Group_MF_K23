import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Create a graph
G = nx.karate_club_graph()
pos = nx.spring_layout(G)

# Initialize the plot
fig, ax = plt.subplots()
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10)

# Function to update the graph on button click
def update_graph(event):
    # Remove an edge (for example, the first edge)
    edges = list(G.edges())
    if edges:
        edge_to_remove = edges[0]
        G.remove_edge(*edge_to_remove)
        fig, ax = plt.subplots()
        # Clear the plot
        ax.clear()

        print('===Draw update graph')
        # Draw the updated graph
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10)

        # Redraw the figure
        #plt.draw()

# Create a button
ax_button = plt.axes([0.81, 0.01, 0.1, 0.05])  # [x, y, width, height]
button = Button(ax_button, 'Remove Edge', color='lightgoldenrodyellow', hovercolor='0.975')

# Attach the button click event handler
button.on_clicked(update_graph)

# Show the plot
plt.show()
