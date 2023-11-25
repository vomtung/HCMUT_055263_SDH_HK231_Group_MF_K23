import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.widgets import Button

# Tạo đồ thị mẫu
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 5), (4, 6), (5, 6), (6, 7)])

# Tính toán cộng đồng sử dụng Girvan-Newman
comp = nx.community.girvan_newman(G)
communities = [c for c in next(comp)]

# Khởi tạo biến để lưu trạng thái hiện tại của cộng đồng
current_step = 0
node_groups = communities[current_step]

# Hàm xử lý sự kiện khi nút được nhấn để hiển thị bước tiếp theo
def show_next_community(event):
    global current_step, node_groups
    if current_step < len(communities) - 1:
        current_step += 1
        node_groups = communities[current_step]
        print("Communities:", node_groups)

        # Vẽ đồ thị với màu sắc biểu thị cộng đồng
        colors = [0] * len(G.nodes())
        for i, group in enumerate(node_groups):
            for node in group:
                colors[node] = i + 1

        plt.clf()
        nx.draw(G, pos=nx.spring_layout(G), node_color=colors, with_labels=True)
        plt.show()

# Tạo figure và trục
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)  # Để tránh nút bị che khuất

# Tạo nút bấm để hiển thị bước tiếp theo
button_ax = plt.axes([0.7, 0.05, 0.1, 0.075])  # Vị trí và kích thước của nút
button = Button(button_ax, 'Next Step')  # Tạo nút với nhãn 'Next Step'

# Gán sự kiện cho nút bấm
button.on_clicked(show_next_community)

# Hiển thị đồ thị với cộng đồng ban đầu
colors = [0] * len(G.nodes())
for i, group in enumerate(node_groups):
    for node in group:
        colors[node] = i + 1

plt.clf()
nx.draw(G, pos=nx.spring_layout(G), node_color=colors, with_labels=True)
plt.show()
