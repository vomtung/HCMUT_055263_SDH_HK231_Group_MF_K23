import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.widgets import Button

# Tạo đồ thị mẫu
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 5), (4, 6), (5, 6), (6, 7)])

# Hàm vẽ lại đồ thị với màu sắc ngẫu nhiên cho các đỉnh
def redraw_graph(event):
    colors = [plt.cm.tab10(i % 10) for i in range(len(G.nodes()))]  # Tạo màu sắc ngẫu nhiên cho mỗi đỉnh
    plt.clf()
    nx.draw(G, pos=nx.spring_layout(G), node_color=colors, with_labels=True)
    plt.show()

# Tạo figure và trục
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)  # Để tránh nút bị che khuất

# Tạo nút bấm để vẽ lại đồ thị với màu sắc mới
button_ax = plt.axes([0.7, 0.05, 0.1, 0.075])  # Vị trí và kích thước của nút
button = Button(button_ax, 'Redraw Graph')  # Tạo nút với nhãn 'Redraw Graph'

# Gán sự kiện cho nút bấm
button.on_clicked(redraw_graph)

# Hiển thị đồ thị ban đầu với màu sắc ngẫu nhiên cho các đỉnh
colors = [plt.cm.tab10(i % 10) for i in range(len(G.nodes()))]  # Tạo màu sắc ngẫu nhiên cho mỗi đỉnh
plt.clf()
nx.draw(G, pos=nx.spring_layout(G), node_color=colors, with_labels=True)
plt.show()
