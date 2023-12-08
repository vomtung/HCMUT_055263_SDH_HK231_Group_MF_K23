import pandas as pd
import csv
import os
import tkinter as tk
from tkinter import filedialog
import networkx as nx
import matplotlib.pyplot as plt
import time

from networkx.algorithms.community import girvan_newman

RUN_STEP =28

# Read the Excel file into a DataFrame
df = pd.read_csv('dataset/studentInfo-50.csv')



#print(df)

G = nx.Graph()
# Display the contents of the DataFrame
#print(df.columns)
for index, row in df.iterrows():
    for index2, row2 in df.iterrows():
        # Access row data using column names or indices
        #print(f"Row[{index}] :", row.values)
        #print(f"Row[{index}] :", row['code_module'])
        #print(f"Row[{index}] ")
        if ((row['code_module'] == row2['code_module'])
                and (row['id_student'] != row2['id_student'])):
            #print(f"id_student:{row['id_student']}", f"id_student2:{row2['id_student']}")
            G.add_edge(row['id_student'], row2['id_student'])



#nx.draw(G, with_labels=True, font_weight='bold')
print("==Finished build graph. Begin run girvan_newman")
# Apply Girvan-Newman algorithm to detect communities
comp = girvan_newman(G)

print("==Finished run girvan_newman", )
draw_community_step = 0
communitiesList = []
for communities_at_step in comp:
    print("== process communities_at_step", draw_community_step, f", RUN_STEP: {RUN_STEP}")
    if draw_community_step == RUN_STEP:
        communitiesList.append(tuple(sorted(c) for c in communities_at_step))
        break
    draw_community_step = draw_community_step + 1

# Get the first set of communities

print( f" draw_community_step{RUN_STEP}")
communities = communitiesList [0]
print(f"==length of community {len(communitiesList)}")

# Create a mapping of nodes to their community index
node_community = {node: idx for idx, comm in enumerate(communities) for node in comm}

# Generate colors for nodes based on communities
node_colors = [node_community[node] for node in G.nodes()]

# Draw the graph, coloring nodes based on communities
pos = nx.spring_layout(G, k=1)
nx.draw(G, pos, node_color=node_colors, with_labels=False, cmap=plt.cm.jet)
plt.show()