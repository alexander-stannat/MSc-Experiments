"""
The code below performs a simulation of a P2P network in which every node will with probability p query a randomly
chosen node. The queried node will then perform work for the node with the highest accounting value out of all the
nodes that have queried it.
For further information read "https://github.com/alexander-stannat/Msc-Thesis/blob/master/Thesis/Report.pdf"
"""

import networkx as nx
import random as rd
import operator
import time
import heapq

class Network(object):
    """

    """

    def __init__(self, nr_nodes, query_probability, nr_rounds, work_size):
        """

        :param nr_nodes:
        :param query_probability:
        :param accounting_mechanism:
        """
        self.graph = nx.DiGraph()
        self.graph.add_nodes_from(range(nr_nodes))
        self.choice_sets = {x: [] for x in self.graph.nodes()}
        self.accounting_values = {x: None for x in self.graph.nodes()}
        self.query_probability = query_probability
        self.nr_rounds = nr_rounds
        self.work_size = work_size
        self.data_consumed = {x: 0 for x in self.graph.nodes()}
        self.data_contributed = {x: 0 for x in self.graph.nodes()}

        self.number_of_queries_made = {x: 0 for x in self.graph.nodes()}
        self.number_of_queries_received = {x: 0 for x in self.graph.nodes()}

    def generate_graph(self):
        """

        :return:
        """
        for round in iter(range(self.nr_rounds)):
            print "Round: ", round + 1
            self.choice_sets = {x: [] for x in iter(self.graph.nodes())}
            self.accounting_values = {x: None for x in iter(self.graph.nodes())}

            for node in iter(self.graph.nodes()):
                nodes = list(self.graph.nodes())
                nodes.remove(node)
                if rd.uniform(0, 1) <= self.query_probability:
                    self.number_of_queries_made[node] += 1
                    self.choice_sets[rd.choice(nodes)].append(node)

            for node in iter(self.graph.nodes()):
                self.number_of_queries_received[node] += len(self.choice_sets[node])

            for node in iter(self.graph.nodes()):
                nodes = list(self.graph.nodes())
                nodes.remove(node)

                """in_out_degrees = [a - b for a, b in
                 zip(dict(self.graph.out_degree(weight='weight')).values(), dict(self.graph.in_degree(weight='weight')).values())]"""

                # self.accounting_values[node] = dict(zip(list(self.graph.nodes()), list(in_out_degrees)))

                # self.accounting_values[node] = nx.pagerank(self.graph, personalization={node: 1}, weight='weight')

                # self.accounting_values[node] = {node1: nx.maximum_flow(self.graph, node, node1, capacity='weight')[1][node] for node1 in iter(nodes)}

                self.accounting_values[node] = {node1: 0 for node1 in nodes}
            for node in iter(self.graph.nodes()):
                if self.choice_sets[node] == []:
                    continue

                """ Winner Takes All """

                """winner_nodes = [x for x in iter(self.choice_sets[node]) if self.accounting_values[node][x] == max(self.accounting_values[node][y] for y in iter(self.choice_sets[node]))]#  self.accounting_values[node].iteritems(), key=operator.itemgetter(1))[1]]
                winner_node = rd.choice(winner_nodes)
                self.data_consumed[winner_node] += self.work_size
                self.data_contributed[node] += self.work_size
                

                print "Node, Choice Set, Winner_nodes: ", node, self.choice_sets[node], winner_nodes
                print "Winner_node: ", winner_node
                if (winner_node, node) in iter(self.graph.edges()):
                    self.graph[winner_node][node]['weight'] += self.work_size
                elif (node, winner_node) in self.graph.edges():
                    self.graph[node][winner_node]['weight'] -= self.work_size
                    if self.graph[node][winner_node]['weight'] == 0:
                        self.graph.remove_edge(node, winner_node)
                    elif self.graph[node][winner_node]['weight'] < 0:
                        self.graph.add_edge(winner_node, node, weight=-self.graph[node][winner_node]['weight'])
                        self.graph.remove_edge(node, winner_node)
                else:
                    self.graph.add_edge(winner_node, node, weight=self.work_size)
                # self.graph.add_weighted_edges_from([(winner_node, node, self.work_size)])
                # self.graph.add_weighted_edges_from([(node, winner_node, self.work_size)])"""



                """ Top 4 (Distribution) """

                winner_nodes = [x for x in iter(self.choice_sets[node]) if self.accounting_values[node][x] in heapq.nlargest(4, [self.accounting_values[node][y] for y in iter(self.choice_sets[node])])]
                self.data_contributed[node] += self.work_size

                print "Node, Choice Set, Winner_nodes: ", node, self.choice_sets[node], winner_nodes

                for winner_node in winner_nodes:
                    self.data_consumed[winner_node] += float(self.work_size) / float(len(winner_nodes))

                    if (node, winner_node) in iter(self.graph.edges()):
                        self.graph[node][winner_node]['weight'] += float(self.work_size) / float(len(winner_nodes))
                    elif (winner_node, node) in self.graph.edges():
                        self.graph[winner_node][node]['weight'] -= float(self.work_size) / float(len(winner_nodes))
                        if self.graph[winner_node][node]['weight'] == 0:
                            self.graph.remove_edge(winner_node, node)
                        elif self.graph[winner_node][node]['weight'] < 0:
                            self.graph.add_edge(node, winner_node, weight=-self.graph[winner_node][node]['weight'])
                            self.graph.remove_edge(winner_node, node)
                    else:
                        self.graph.add_edge(node, winner_node, weight=(float(self.work_size) / float(len(winner_nodes))))
                    # self.graph.add_weighted_edges_from([(node, winner_node, self.work_size)])
                    # self.graph.add_weighted_edges_from([(winner_node, node, self.work_size)])


                """ Top 4 (No Distribution) """

                """winner_nodes = [x for x in iter(self.choice_sets[node]) if self.accounting_values[node][x] in heapq.nlargest(4, [self.accounting_values[node][y] for y in iter(self.choice_sets[node])])]
                self.data_contributed[node] += (self.work_size*len(winner_nodes))

                print "Node, Choice Set, Winner_nodes: ", node, self.choice_sets[node], winner_nodes

                for winner_node in winner_nodes:
                    self.data_consumed[winner_node] += self.work_size
                    print "Data consumed by", winner_node, " : ", self.data_consumed[winner_node]

                    if (node, winner_node) in iter(self.graph.edges()):
                        self.graph[node][winner_node]['weight'] += self.work_size
                    elif (winner_node, node) in self.graph.edges():
                        self.graph[winner_node][node]['weight'] -= self.work_size
                        if self.graph[winner_node][node]['weight'] == 0:
                            self.graph.remove_edge(winner_node, node)
                        elif self.graph[winner_node][node]['weight'] < 0:
                            self.graph.add_edge(node, winner_node, weight=-self.graph[winner_node][node]['weight'])
                            self.graph.remove_edge(winner_node, node)
                    else:
                        self.graph.add_edge(node, winner_node, weight=self.work_size)
                    # self.graph.add_weighted_edges_from([(node, winner_node, self.work_size)])
                    # self.graph.add_weighted_edges_from([(winner_node, node, self.work_size)])"""


                """ Distribution """

                """winner_nodes = self.choice_sets[node]
                self.data_contributed[node] += self.work_size
                accounting_values_of_choice_set = {winner_node: self.accounting_values[node][winner_node] for winner_node in winner_nodes}
                sorted_winner_nodes = dict(sorted(accounting_values_of_choice_set.items(), key=lambda x: x[1], reverse=True))

                print accounting_values_of_choice_set
                print "Node, Choice Set, Winner_nodes: ", node, self.choice_sets[node], winner_nodes
                i = 0
                for winner_node in sorted_winner_nodes.keys():
                    i += 1
                    self.data_consumed[winner_node] += (float(i) * float(self.work_size)) / float(sum(range(len(sorted_winner_nodes) + 1)))

                    if (node, winner_node) in iter(self.graph.edges()):
                        self.graph[node][winner_node]['weight'] += float(self.work_size) / float(len(winner_nodes))
                    elif (winner_node, node) in self.graph.edges():
                        self.graph[winner_node][node]['weight'] -= float(self.work_size) / float(len(winner_nodes))
                        if self.graph[winner_node][node]['weight'] == 0:
                            self.graph.remove_edge(winner_node, node)
                        elif self.graph[winner_node][node]['weight'] < 0:
                            self.graph.add_edge(node, winner_node, weight=-self.graph[winner_node][node]['weight'])
                            self.graph.remove_edge(winner_node, node)
                    else:
                        self.graph.add_edge(node, winner_node,
                                            weight=(float(self.work_size) / float(len(winner_nodes))))
                    # self.graph.add_weighted_edges_from([(node, winner_node, self.work_size)])
                    # self.graph.add_weighted_edges_from([(winner_node, node, self.work_size)])"""

        return self.graph




