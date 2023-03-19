#1. Використовуючи дані із файлу cities. csv, створять список типу  cities=[['city1.city2, km]...].  отриманого списку створіть граф.
# Візуалізуйте отриманий граф.
import csv
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'cities1.csv', sep=';')
print(df.head(5))

G = nx.Graph()
list_of_nodes1 = [(x,y,z) for x,y,z in df.values.tolist()]

list_of_nodes = list_of_nodes1[0:2]
print(list_of_nodes[0:2])
G.add_edges_from(list_of_nodes)
#
# nx.draw_random(G,  node_size= 1000 , with_labels=True)

sub_G = list(nx.connected_component_subgraphs(G))
edges_ = []
for sub in sub_G:
    edges = sub.edges()
    if len(edges) > 1:
        print(edges, "всего связей в подгруппах: %s" %len(edges))
        for node in edges:
            edges_.append(node)

G_ = nx.Graph()
G_.add_edges_from(edges_)
nx.draw(G_, pos=nx.spring_layout(G_), node_size= 1000 , font_size=50, with_labels=True)
plt.show()

# plt.show()
# df = []
# with open('cities.csv') as File:
#     reader = csv.reader(File)
#     for row in reader:
#         df.append(row)
#     # print(df)
#
# G = nx.DiGraph()
# G.add_weighted_edges_from([('Hadiach','Zinkiv',45), ('Zinkiv','Hadiach',45), ('Hadiach','Lebedyn',60)])
# predecessors, _ = nx.floyd_warshall_predecessor_and_distance(G)
# # кратчайший путь от вершины [s] к вершине [v]
# shortest_path_s_v = nx.reconstruct_path('Hadiach', 'Zinkiv', predecessors)
# print(shortest_path_s_v)
# # список ребер кратчайшего пути
# edges = [(a,b) for a,b in zip(shortest_path_s_v, shortest_path_s_v[1:])]
# # список всех весов ребер
# weights = nx.get_edge_attributes(G, 'weight')
# print(weights)
# # позиции вершин для визуализации графа
# #pos = nx.spring_layout(G)
# pos = nx.circular_layout(G)
# print(pos)
# # рисуем граф
# nx.draw_networkx(G, pos=pos)
# # рисуем веса ребер
# nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
# # рисуем кратчайший путь: [s] -> [v]
# nx.draw_networkx_edges(G, pos=pos, edgelist=edges, edge_color="r", width=3)
# # заголовок графика
# title = "Shortest path between [{}] and [{}]: {}"\
#         .format("s", "v", " -> ".join(shortest_path_s_v))
# plt.title(title)

# 2. Напишіть функцію знаходження найкоротшого маршруту між двома населенними пунктами, яка приймає у якості
# аргументів об'єкт графу і пару населенніх пунктів, а повертає маршрут і його протяжність.