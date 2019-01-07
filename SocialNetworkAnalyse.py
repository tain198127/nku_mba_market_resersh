# -*- coding: UTF-8 -*-
import logging
import string
import networkx as nx
import os
import random
import sys
import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter
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
                logging.debug(l.strip().split(','))
                raw_data.append(l.strip().split(','))
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

    def __tograph(self, nodes, edges):
        """
        返回图对象
        :param nodes:节点，一维数组
        :param edges: 变数组，二维数组
        :return: 图对象
        """
        g = nx.DiGraph()
        # g.add_nodes_from(nodes)
        g.add_edges_from(edges)
        return g

    def __draw(self, g):
        """
        画图
        :param g: networkx 的图
        :return:
        """
        nx.draw(g, pos=nx.random_layout(g), node_color='b', edge_color='r', with_labels=True, font_size=10,
                font_weight='bold', node_size=20, style='solid', arrows=True)
        plt.show()

    def __analyse(self, g):
        """
        分析
        :param g:图
        :return:经过排序的各种度量，按照顺序分别是degree,between,closing三个维度
        """
        degree_score = nx.degree_centrality(g)
        logging.debug("程度中心性")
        sort_degree_score = sorted(degree_score.items(), key=lambda x: x[1], reverse=True)
        logging.debug(sort_degree_score)

        between_score = nx.betweenness_centrality(g)
        sort_between_score = sorted(between_score.items(), key=lambda x: x[1], reverse=True)
        logging.debug("中介中心性")
        logging.debug(sort_between_score)

        close_score = nx.closeness_centrality(g)
        sort_close_score = sorted(close_score.items(), key=lambda x: x[1], reverse=True)
        logging.debug("接近中心性")
        logging.debug(sort_close_score)
        return sort_degree_score, sort_between_score, sort_close_score

    def __write2excel(self, degree, between, close, path):
        """
        将分析结果写入到excel中
        :param degree:程度中心度
        :param between:中介中心度
        :param close:接近中心度
        :param path:文档路径
        :return:
        """
        wb = xlsxwriter.Workbook(path)
        sheet1 = wb.add_worksheet(name="degree程度中心性")
        sheet1.write_row('A1', data=["学号", "程度中心度"])
        for row_num, pre_degree in enumerate(degree):
            # logging.debug(pre_degree[0])
            # logging.debug(round(pre_degree[1],10))
            line = row_num + 1
            sheet1.write_row(line, 0, pre_degree)

        sheet2 = wb.add_worksheet(name="between中介中心性")
        sheet2.write_row('A1', data=["学号", "中介中心度"])
        for row_num, pre_between in enumerate(between):
            # logging.debug(pre_between[0])
            # logging.debug(round(pre_between[1],10))
            line = row_num + 1
            sheet2.write_row(line, 0, pre_between)

        sheet3 = wb.add_worksheet(name="close接近中心性")
        sheet3.write_row('A1', data=["学号", "接近中心度"])
        for row_num, pre_close in enumerate(close):
            # logging.debug(pre_close[0])
            # logging.debug(round(pre_close[1],10))
            line = row_num + 1
            sheet3.write_row(line, 0, pre_close)

        wb.close()

    def main(self, path):
        nodes, edges = self.__loaddata(path)
        # 得到节点和边
        # g = nx.read_pajek('/Users/tain/Desktop/Pajek/final20190107.net')
        # 不太好用，读不进来

        g = self.__tograph(nodes, edges)
        # 得到图
        nx.write_pajek(g,'pajek.net')
        # 把图写到pajek模式中去

        self.__draw(g)
        # 可以画出来
        degree, between, close = self.__analyse(g)

        # 还可以分析数据
        self.__write2excel(degree, between, close,
                           '/Users/tain/Develop/python/market_analyse/final_social_network.xlsx')


def main():
    sna = SocialNetworkAnalyse()
    sna.main('/Users/tain/Develop/python/market_analyse/汇总final final20190107.txt')


if __name__ == '__main__':
    main()
