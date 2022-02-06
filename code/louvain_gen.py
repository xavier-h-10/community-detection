# louvain示意图生成
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


edge0 = [
    (0, 2), (0, 3), (0, 4), (0, 5),
    (1, 2), (1, 4), (1, 7),
    (2, 4), (2, 5), (2, 6),
    (3, 7),
    (4, 10),
    (5, 7), (5, 11),
    (6, 7), (6, 11),
    (8, 9), (8, 10), (8, 11), (8, 14), (8, 15),
    (9, 12), (9, 14),
    (10, 11), (10, 12), (10, 13), (10, 14),
    (11, 13)
]


def graph0(nodes):
    g = nx.Graph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edge0, weight=1)
    return g


def graph1():
    g = nx.Graph()
    g.add_edge(0, 1, weight=4)
    g.add_edge(0, 2, weight=1)
    g.add_edge(0, 3, weight=1)
    g.add_edge(1, 2, weight=1)
    g.add_edge(2, 3, weight=3)
    return g


def graph2():
    g = nx.Graph()
    g.add_nodes_from([0, 1, 2, 3])
    g.add_edge(0, 2, weight=3)
    return g


def pass0():
    g = graph0(range(16))
    pos = nx.circular_layout(g)
    nx.draw(g, pos, with_labels=True, edge_color='b', node_color=range(len(g.nodes())), node_size=500, cmap=plt.cm.cool)
    plt.show()


def pass1_phase1():
    g = graph0([0, 1, 2, 4, 5, 3, 6, 7, 11, 13, 8, 9, 10, 12, 14, 15])
    pos = nx.circular_layout(g)
    color = [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3]
    nx.draw(g, pos, with_labels=True, edge_color='b', node_color=color, node_size=500, cmap=plt.cm.cool)
    plt.show()


def pass1_phase2():
    g = graph1()
    edge_labels = dict([((u, v,), d['weight']) for u, v, d in g.edges(data=True)])
    pos = nx.circular_layout(g)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=20)
    nx.draw(g, pos, with_labels=True, edge_color='b', node_color=range(len(g.nodes())), node_size=550, cmap=plt.cm.cool)
    plt.show()


def pass2():
    g = graph2()
    edge_labels = dict([((u, v,), d['weight']) for u, v, d in g.edges(data=True)])
    pos = nx.circular_layout(g)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=20)
    nx.draw(g, pos, with_labels=True, edge_color='b', node_color=range(len(g.nodes())), node_size=1000, cmap=plt.cm.cool)
    plt.show()


if __name__ == '__main__':
    pass2()
