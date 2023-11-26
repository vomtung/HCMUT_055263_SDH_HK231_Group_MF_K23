import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from networkx.algorithms.community import girvan_newman

# Create a graph
G = nx.karate_club_graph()
pos = nx.spring_layout(G)

# Initialize the plot
fig, ax = plt.subplots()
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10)

# Girvan-Newman algorithm generator
gn_gen = girvan_newman(G)

# Function to update the plot in each animation frame
def update(frame):
    try:
        # Get the next step of the Girvan-Newman algorithm
        communities = next(gn_gen)

        # Clear the plot
        ax.clear()

        # Draw the updated graph with communities
        colors = [0] * G.number_of_nodes()
        for i, community in enumerate(communities):
            for node in community:
                colors[node] = i
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color=colors, cmap=plt.cm.rainbow, font_color='black', font_size=10)

        # Display additional information (optional)
        ax.set_title(f"Step {frame + 1}")

    except StopIteration:
        pass

# Create an animation
animation = FuncAnimation(fig, update, frames=range(G.number_of_edges() - 1), repeat=False)

# Show the plot
plt.show()