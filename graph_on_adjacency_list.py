#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from graphviz import Graph
import string


class AdjListGraph:
    def __init__(self):
        self.adj = list()  # Список смежности
        self.attributes = list()  # Список атрибутов вершин, list of dict

    def add_vertices(self, n):
        """ Добавить n вершн в граф.

        :param int n: колиичество вершин для добавления
        """
        for i in range(n):
            self.adj.append(set()) #Тут сет, а не лист
            self.attributes.append(dict())

    def number_of_vertices(self):
        """ Возвращает количество вершин графа

        :rtype: int
        """
        return len(self.adj)

    def remove_vertex(self, v):
        """ Удалить вершину из графа

        :param int v: индекс вершины графа
        """

#        print(v,(len(self.adj)-1))
#        assert ((v < len(self.adj)) and (v > -1)), "This vertex is not in graph"
        if (v in [x for x in range(len(self.adj)+1)]):
            self.adj.pop(v)
            self.attributes.pop(v)
        else:
            print("Vertex is not in graph")


    def add_edge(self, u, v):
        """ Добавить ребро, соединяющее вершины с индексами u и v

        :param int u: индекс вершины графа
        :param int v: индекс вершины графа
        """
        if (v in [x for x in range(len(self.adj)+1)]) and \
           (u in [x for x in range(len(self.adj)+1)]):
               self.adj[u].add(v)
               self.adj[v].add(u)
        else:
            print('Check your vertices')

    def remove_edge(self, u, v):
        """ Удалить ребро, соединяющее вершины с индексами u и v

        :param int u: индекс вершины графа
        :param int v: индекс вершины графа
        """
        try:
            self.adj[u].remove(v)
            self.adj[v].remove(u)
        except:
            print('Probably, smth goes wrong, check it again')

    def number_of_edges(self):
        """ Возвращает количество ребер в графе

        :rtype: int
        """
        count=0
        for i in range(len(self.adj)):
            count+=len(self.adj[i])
        return int(count/2)
#        raise NotImplemented("Реализуйте этот метод")

    def neighbors(self, v):
        """ Возвращает список индексов вершин, соседних с данной

        :param int v: индекс вершины графа
        :rtype: list of int
        """
        return self.adj[v]
#        raise NotImplemented("Реализуйте этот метод")

    def draw(self, filename='test.gv'):
        """
        Отрисовывает граф используя библиотеку Graphviz. Больше примеров:
        https://graphviz.readthedocs.io/en/stable/examples.html
        """
        g = Graph('G', filename=filename, engine='sfdp')

        for v, attr in enumerate(self.attributes):
            if 'color' in attr:
                g.attr('node', style='filled', fillcolor=attr['color'])
                if attr['color'] == 'black':
                    g.attr('node', fontcolor='white')
            else:
                g.attr('node', style='', color='', fontcolor='', fillcolor='')

            if 'name' in attr:
                g.node(str(v), label='{} ({})'.format(attr['name'], v))
            else:
                g.node(str(v))

        for i in range(self.number_of_vertices()):
            for j in self.adj[i]:
                if i < j:
                    g.edge(str(i), str(j))
        g.view()


def main():
    g = AdjListGraph()
    count_vertices=6
    colour=("blue","green","white","red","yellow","orange")
    g.add_vertices(count_vertices)
    for i, c, z in zip(range(count_vertices), string.ascii_lowercase, colour):
        g.attributes[i]['name'] = c
        g.attributes[i]['colour'] = z
    print(g.number_of_vertices())
    print(g.attributes)
    print(g.adj)
    print(g.attributes)
    g.remove_vertex(0)
    print(g.attributes)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

#    g.remove_edge(1, 2)

    print(g.number_of_edges())
    print(g.number_of_vertices())
    print(g.neighbors(1))
    print(g.adj)
    g.draw()


if __name__ == "__main__":
    main()
