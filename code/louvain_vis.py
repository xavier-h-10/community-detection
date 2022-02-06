# louvain可视化, 需要ffmpeg库
import numpy as np
from communities.algorithms import louvain_method
import networkx as nx
from communities.visualization import louvain_animation, draw_communities
import matplotlib.pyplot as plt

G = nx.karate_club_graph()  # 采用 Zachary's karate club数据集进行可视化
G = G.to_undirected()

N = len(G.adj)
A = np.zeros((N, N))
for i in range(len(G.adj)):
    nodeList = list(G.adj[i])
    for j in nodeList:
        A[i][j] = 1

adj_matrix = A

communities, frames = louvain_method(adj_matrix)
louvain_animation(adj_matrix, frames)
plt.show()

