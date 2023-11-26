import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.widgets import Button

from Service.ExcelService import ExcelService

p = ExcelService()

# Tạo đồ thị mẫu
#G = nx.Graph()
#G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 5), (4, 6), (5, 6), (6, 7)])
#G = nx.karate_club_graph()
G = p.readRegistrationInfoToGraph()

# Tính toán cộng đồng sử dụng Girvan-Newman
comp = nx.community.girvan_newman(G)
communities = []
for communities_at_step in comp:
    communities.append(tuple(sorted(c) for c in communities_at_step))

# Khởi tạo biến để lưu trạng thái hiện tại của cộng đồng
current_step = 0
node_groups = communities[current_step]

# Hàm vẽ đồ thị và cộng đồng tương ứng
def draw_graph_with_community():
    colors = [0] * len(G.nodes())
    for i, group in enumerate(node_groups):
        for node in group:
            colors[node - 1] = i + 1

    plt.clf()
    nx.draw(G, node_color=colors, with_labels=True)
    plt.show()

# Hàm xử lý sự kiện khi nút được nhấn để hiển thị bước tiếp theo
def show_next_community(event):
    global current_step, node_groups
    if current_step < len(communities) - 1:
        current_step += 1
        node_groups = communities[current_step]
        print("Communities:", node_groups)
        draw_graph_with_community()
    else:
        print("current_step:" + str(current_step) +" len(communities):" + str(len(communities)))

# Tạo figure và trục
fig, ax = plt.subplots()
#plt.subplots_adjust(bottom=0.2)  # Để tránh nút bị che khuất

# Tạo nút bấm để hiển thị bước tiếp theo
button_ax = plt.axes([0.81, 0.01, 0.1, 0.05])
button = Button(button_ax, 'Next Step')  # Tạo nút với nhãn 'Next Step'



# Gán sự kiện cho nút bấm
button.on_clicked(show_next_community)




# Hiển thị đồ thị với cộng đồng ban đầu
draw_graph_with_community()
