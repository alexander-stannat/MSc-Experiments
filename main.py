from Accounting_Values_Simulation import Network
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pickle

network = Network(100, 0.7, 1000, 1)
graph = network.generate_graph()
# pos = nx.spring_layout(graph)
# nx.draw(graph, with_labels=True, pos=pos, node_size=200)
# plt.show()"""

# print network.accounting_values"""
"""
sns.set_style('whitegrid')
# sns.kdeplot(np.array(network.accounting_values[network.graph.nodes()[0]].values()), bw=0.5)
plt.title("Deg Values")
plt.show()
"""
"""
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=labels)
plt.show()

print list(graph.nodes())
print graph.in_degree(weight='weight')
"""

"""
plt.hist(network.data_consumed.values(), bins=100, stacked=True)
plt.title("Data Consumed")
plt.show()
plt.hist(network.data_contributed.values(), bins=100, stacked=True)
plt.title("Data Contributed")
plt.show()

sns.set_style('whitegrid')
sns.kdeplot(np.array(network.data_consumed.values()), bw=0.5)
plt.title("Data Consumed")
plt.show()
sns.kdeplot(np.array(network.data_contributed.values()), bw=0.5)
plt.title("Data Contributed")
plt.show()
"""
"""
fig = plt.figure(figsize=(20, 7))
fig.suptitle('Accounting Mechanism: 0s \n Allocation Policy: Top 4 (Distribution) \n     \n    ', fontsize=15)
plt.get_current_fig_manager().window.wm_geometry("+0+0")
sns.set_style('whitegrid')

plt.subplot(2, 2, 1)
plt.hist(network.data_consumed.values(), bins=100, stacked=True, label="Data Consumed")
plt.title("Data Consumed and Contributed (Histogramme)")
plt.hist(network.data_contributed.values(), bins=100, stacked=True, label="Data Contributed")
plt.legend()

plt.subplot(2, 2, 2)
sns.kdeplot(np.array(network.data_consumed.values()), bw=0.5, legend="Data Consumed")
sns.kdeplot(np.array(network.data_contributed.values()), bw=0.5, legend="Data Contributed")
plt.title("Data Consumed and Contributed (Density Plot)")

plt.subplot(2, 2, 3)
plt.hist([a-b for a, b in zip(network.data_consumed.values(), network.data_contributed.values())], bins=100, stacked=True)
plt.title("Data Consumed - Data Contributed")

plt.subplot(2, 2, 4)
sns.kdeplot(np.array([a-b for a, b in zip(network.data_consumed.values(), network.data_contributed.values())]), bw=0.5)
plt.title("Data Consumed - Data Contributed")
plt.show()
"""
"""
file_name = "Simulation Values PGR Winner"
fileObject = open(file_name, 'wb')
pickle.dump([network.data_consumed, network.data_contributed], fileObject)
fileObject.close()
"""
"""
file_name = "Simulation Values PGR Winner"
fileObject = open(file_name, 'r')
[data_consumed, data_contributed] = pickle.load(fileObject)
fileObject.close()

fig = plt.figure(figsize=(20, 7))
fig.suptitle('Accounting Mechanism: PGR \n Allocation Policy: Winner \n     \n    ', fontsize=15)
plt.get_current_fig_manager().window.wm_geometry("+0+0")
sns.set_style('whitegrid')

plt.subplot(2, 2, 1)
plt.hist(data_consumed.values(), bins=100, stacked=True, label="Data Consumed")
plt.title("Data Consumed and Contributed (Histogramme)")
plt.hist(data_contributed.values(), bins=100, stacked=True, label="Data Contributed")
plt.legend()

plt.subplot(2, 2, 2)
sns.kdeplot(np.array(data_consumed.values()), bw=0.5, legend="Data Consumed")
sns.kdeplot(np.array(data_contributed.values()), bw=0.5, legend="Data Contributed")
plt.title("Data Consumed and Contributed (Density Plot)")

plt.subplot(2, 2, 3)
plt.hist([a-b for a, b in zip(data_consumed.values(), data_contributed.values())], bins=100, stacked=True)
plt.title("Data Consumed - Data Contributed")

plt.subplot(2, 2, 4)
sns.kdeplot(np.array([a-b for a, b in zip(data_consumed.values(), data_contributed.values())]), bw=0.5)
plt.title("Data Consumed - Data Contributed")
plt.show()
"""

"""
file_name = "Simulation Values PGR Winner" # This needs to be changed
fileObject = open(file_name, 'r')
[data_consumed, data_contributed] = pickle.load(fileObject)
fileObject.close()

fig = plt.figure(figsize=(20, 4))
fig.suptitle('Accounting Mechanism: PGR \n Allocation Policy: Winner Takes All \n     \n    ', fontsize=15) # This needs to be changed
plt.get_current_fig_manager().window.wm_geometry("+0+0")
sns.set_style('whitegrid')

plt.subplot(1, 2, 1)
sns.kdeplot(np.array(data_consumed.values()), bw=0.5, label="Data Consumed")
sns.kdeplot(np.array(data_contributed.values()), bw=0.5, label="Data Contributed")
plt.xlabel('Amount of Data Consumed and Contributed (in MB)')
plt.ylabel('Proportion of Network Nodes')
plt.legend()
# plt.title("Data Consumed and Contributed (Density Plot)")

plt.subplot(1, 2, 2)
sns.kdeplot(np.array([a-b for a, b in zip(data_consumed.values(), data_contributed.values())]), bw=0.5)
plt.xlabel('Amount of Data Consumed minus amount of Data Contributed (in MB)')
plt.ylabel('Proportion of Network Nodes')
# plt.title("Data Consumed - Data Contributed (Density Plot)")

plt.subplots_adjust(top=0.85)
plt.show()
"""



fig = plt.figure(figsize=(10, 5))
fig.suptitle('Queries Made and Received by Nodes in the Simulation (Density Plots) \n     \n    ', fontsize=15)
plt.get_current_fig_manager().window.wm_geometry("+0+0")

plt.subplot(1, 2, 1)
#sns.set_style('whitegrid')
sns.kdeplot(np.array(network.number_of_queries_received.values()), bw=0.5, label="Queries Received")
sns.kdeplot(np.array(network.number_of_queries_made.values()), bw=0.5, label="Queries Made")
# plt.title("Queries Made and Received (Density Plot)")
plt.xlabel('Nr. of Queries made and received')
plt.ylabel('Proportion of Network Nodes')
plt.legend()


plt.subplot(1, 2, 2)
#sns.set_style('whitegrid')
sns.kdeplot(np.array(network.number_of_queries_made.values()) - np.array(network.number_of_queries_received.values()), bw=0.5, legend="Queries made - queries received")
# plt.title("Queries Received - Queries Made (Density Plot)")
plt.xlabel('Nr. of Queries Made minus Nr. of Queries Received')
plt.ylabel('Proportion of Network Nodes')
plt.show()



