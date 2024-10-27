import networkx as nx
import matplotlib.pyplot as plt

# Tạo đồ thị
G = nx.Graph()

# Danh sách các thành phố và các chuyến bay
flights = [
    ("Hà Nội", "TP HCM"),
    ("Hà Nội", "Đà Nẵng"),
    ("Hà Nội", "Nha Trang"),
    ("TP HCM", "Đà Nẵng"),
    ("TP HCM", "Nha Trang"),
    ("Đà Nẵng", "Nha Trang"),
    ("Hà Nội", "Cần Thơ"),
    ("TP HCM", "Cần Thơ")
]

# Thêm các chuyến bay vào đồ thị
G.add_edges_from(flights)

# Vẽ đồ thị
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)  # Vị trí các nút
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_color='black', font_weight='bold', edge_color='gray')
plt.title('Đồ Thị Các Chuyến Bay Từ Các Thành Phố Lớn Ở Việt Nam')
plt.show()