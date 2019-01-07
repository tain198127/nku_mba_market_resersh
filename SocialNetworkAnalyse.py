# -*- coding: UTF-8 -*-
import logging
import string
import networkx as nx
import os
import random
import sys
import matplotlib.pyplot as plt
import numpy as np
import sklearn

logging.basicConfig(level=logging.DEBUG)


class SocialNetworkAnalyse:
    def __init__(self):
        print('ok')

    def __loaddata(self, path):
        """
        加载数据
        :param path: 数据地址
        :return: nodes和line
        """
        raw_data = []
        nodes = []
        edge = []
        try:
            f = open(path)
            for l in f.readlines():
                ld = l.strip().split(',')
                ay = [int(ld[0]), int(ld[1])]
                logging.debug(ay)
                raw_data.append(ay)
        finally:
            f.close()
        m = np.matrix(raw_data).flatten().reshape(-1).tolist()[0]
        nodes = list(set(m))
        for e in raw_data:
            edge.append(e)
        logging.debug(m)
        logging.debug(nodes)
        logging.debug(edge)
        return nodes, edge

    def __tograph(self,nodes,edges):
        """
        返回图对象
        :param nodes:节点，一维数组
        :param edges: 变数组，二维数组
        :return: 图对象
        """
        g = nx.MultiDiGraph()
        # g.add_nodes_from(nodes)
        g.add_edges_from(edges)
        return g

    def main(self, path):
        nodes, edges = self.__loaddata(path)
        g = self.__tograph(nodes,edges)

        nx.draw(g,pos=nx.random_layout(g),node_color='b',edge_color='r', with_labels=True,font_size=10,font_weight='bold', node_size=20)
        # nx.draw_shell(g)
        plt.show()
        print('main')


def main():
    sna = SocialNetworkAnalyse()
    sna.main('/Users/tain/Develop/python/market_analyse/汇总final final20190107.txt')


if __name__ == '__main__':
    main()
