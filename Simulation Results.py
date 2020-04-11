import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values PGR Winner"
fileObject = open(file_name, 'rb')
data_cons_data_cont_0s_top_n_dist = pickle.load(fileObject)
fileObject.close()

fig = plt.figure(figsize=(20, 7))
fig.suptitle('Accounting Mechanism: PGR \n Allocation Policy: Winner \n     \n    ', fontsize=15)
plt.get_current_fig_manager().window.wm_geometry("+0+0")

plt.subplot(2, 2, 1)
plt.hist(data_cons_data_cont_0s_top_n_dist[0].values(), bins=100, stacked=True, label="Data Consumed")
plt.title("Data Consumed and Contributed (Histogramme)")
plt.hist(data_cons_data_cont_0s_top_n_dist[1].values(), bins=100, stacked=True, label="Data Contributed")
plt.legend()

plt.subplot(2, 2, 2)
sns.set_style('whitegrid')
sns.kdeplot(np.array(data_cons_data_cont_0s_top_n_dist[0].values()), bw=0.5, legend="Data Consumed")
sns.kdeplot(np.array(data_cons_data_cont_0s_top_n_dist[1].values()), bw=0.5, legend="Data Contributed")
plt.title("Data Consumed and Contributed (Density Plot)")


plt.subplot(2, 2, 3)
plt.hist([a-b for a, b in zip(data_cons_data_cont_0s_top_n_dist[0].values(), data_cons_data_cont_0s_top_n_dist[1].values())], bins=100, stacked=True)
plt.title("Data Consumed - Data Contributed")


plt.subplot(2, 2, 4)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_0s_top_n_dist[0].values(), data_cons_data_cont_0s_top_n_dist[1].values())]), bw=0.5)
plt.title("Data Consumed - Data Contributed")
plt.show()



"""
file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values 0s, Winner"
fileObject = open(file_name, 'rb')
data_cons_data_cont_0s_winner = pickle.load(fileObject)
fileObject.close()

fig = plt.figure(figsize=(20, 7))
fig.suptitle('Accounting Mechanism: 0s \n Allocation Policy: Winner Takes All \n     \n    ', fontsize=15)
plt.get_current_fig_manager().window.wm_geometry("+0+0")

plt.subplot(2, 2, 1)
plt.hist(data_cons_data_cont_0s_winner[0].values(), bins=100, stacked=True, label="Data Consumed")
plt.title("Data Consumed and Contributed (Histogramme)")
plt.hist(data_cons_data_cont_0s_winner[1].values(), bins=100, stacked=True, label="Data Contributed")
plt.legend()

plt.subplot(2, 2, 2)
sns.set_style('whitegrid')
sns.kdeplot(np.array(data_cons_data_cont_0s_winner[0].values()), bw=0.5, legend="Data Consumed")
sns.kdeplot(np.array(data_cons_data_cont_0s_winner[1].values()), bw=0.5, legend="Data Contributed")
plt.title("Data Consumed and Contributed (Density Plot)")


plt.subplot(2, 2, 3)
plt.hist([a-b for a, b in zip(data_cons_data_cont_0s_winner[0].values(), data_cons_data_cont_0s_winner[1].values())], bins=100, stacked=True)
plt.title("Data Consumed - Data Contributed")


plt.subplot(2, 2, 4)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_0s_winner[0].values(), data_cons_data_cont_0s_winner[1].values())]), bw=0.5)
plt.title("Data Consumed - Data Contributed")
plt.show()



file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values 0s Top n (No Distribution)"
fileObject = open(file_name, 'rb')
data_cons_data_cont_0s_top_n_nodist = pickle.load(fileObject)
fileObject.close()

fig = plt.figure(figsize=(20, 7))
fig.suptitle('Accounting Mechanism: 0s \n Allocation Policy: Top 4 (No Distribution) \n     \n    ', fontsize=15)
plt.get_current_fig_manager().window.wm_geometry("+0+0")

plt.subplot(2, 2, 1)
plt.hist(data_cons_data_cont_0s_top_n_nodist[0].values(), bins=100, stacked=True, label="Data Consumed")
plt.title("Data Consumed and Contributed (Histogramme)")
plt.hist(data_cons_data_cont_0s_top_n_nodist[1].values(), bins=100, stacked=True, label="Data Contributed")
plt.legend()

plt.subplot(2, 2, 2)
sns.set_style('whitegrid')
sns.kdeplot(np.array(data_cons_data_cont_0s_top_n_nodist[0].values()), bw=0.5, legend="Data Consumed")
sns.kdeplot(np.array(data_cons_data_cont_0s_top_n_nodist[1].values()), bw=0.5, legend="Data Contributed")
plt.title("Data Consumed and Contributed (Density Plot)")


plt.subplot(2, 2, 3)
plt.hist([a-b for a, b in zip(data_cons_data_cont_0s_top_n_nodist[0].values(), data_cons_data_cont_0s_top_n_nodist[1].values())], bins=100, stacked=True)
plt.title("Data Consumed - Data Contributed")


plt.subplot(2, 2, 4)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_0s_top_n_nodist[0].values(), data_cons_data_cont_0s_top_n_nodist[1].values())]), bw=0.5)
plt.title("Data Consumed - Data Contributed")
plt.show()




file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values 0s Distribution"
fileObject = open(file_name, 'rb')
data_cons_data_cont_0s_dist = pickle.load(fileObject)
fileObject.close()

fig = plt.figure(figsize=(20, 7))
fig.suptitle('Accounting Mechanism: 0s \n Allocation Policy: Distribution \n     \n    ', fontsize=15)
plt.get_current_fig_manager().window.wm_geometry("+0+0")

plt.subplot(2, 2, 1)
plt.hist(data_cons_data_cont_0s_dist[0].values(), bins=100, stacked=True, label="Data Consumed")
plt.title("Data Consumed and Contributed (Histogramme)")
plt.hist(data_cons_data_cont_0s_dist[1].values(), bins=100, stacked=True, label="Data Contributed")
plt.legend()

plt.subplot(2, 2, 2)
sns.set_style('whitegrid')
sns.kdeplot(np.array(data_cons_data_cont_0s_dist[0].values()), bw=0.5, legend="Data Consumed")
sns.kdeplot(np.array(data_cons_data_cont_0s_dist[1].values()), bw=0.5, legend="Data Contributed")
plt.title("Data Consumed and Contributed (Density Plot)")


plt.subplot(2, 2, 3)
plt.hist([a-b for a, b in zip(data_cons_data_cont_0s_dist[0].values(), data_cons_data_cont_0s_dist[1].values())], bins=100, stacked=True)
plt.title("Data Consumed - Data Contributed")


plt.subplot(2, 2, 4)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_0s_dist[0].values(), data_cons_data_cont_0s_dist[1].values())]), bw=0.5)
plt.title("Data Consumed - Data Contributed")
plt.show()






file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values Deg Top n (Distribution)"
fileObject = open(file_name, 'rb')
data_cons_data_cont_Deg_top_n_dist = pickle.load(fileObject)
fileObject.close()

fig = plt.figure(figsize=(20, 7))
fig.suptitle('Accounting Mechanism: Deg \n Allocation Policy: Top 4 (Distribution) \n     \n    ', fontsize=15)
plt.get_current_fig_manager().window.wm_geometry("+0+0")

plt.subplot(2, 2, 1)
plt.hist(data_cons_data_cont_Deg_top_n_dist[0].values(), bins=100, stacked=True, label="Data Consumed")
plt.title("Data Consumed and Contributed (Histogramme)")
plt.hist(data_cons_data_cont_Deg_top_n_dist[1].values(), bins=100, stacked=True, label="Data Contributed")
plt.legend()

plt.subplot(2, 2, 2)
sns.set_style('whitegrid')
sns.kdeplot(np.array(data_cons_data_cont_Deg_top_n_dist[0].values()), bw=0.5, legend="Data Consumed")
sns.kdeplot(np.array(data_cons_data_cont_Deg_top_n_dist[1].values()), bw=0.5, legend="Data Contributed")
plt.title("Data Consumed and Contributed (Density Plot)")


plt.subplot(2, 2, 3)
plt.hist([a-b for a, b in zip(data_cons_data_cont_Deg_top_n_dist[0].values(), data_cons_data_cont_Deg_top_n_dist[1].values())], bins=100, stacked=True)
plt.title("Data Consumed - Data Contributed")


plt.subplot(2, 2, 4)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_Deg_top_n_dist[0].values(), data_cons_data_cont_Deg_top_n_dist[1].values())]), bw=0.5)
plt.title("Data Consumed - Data Contributed")
plt.show()




file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values Deg, Winner"
fileObject = open(file_name, 'rb')
data_cons_data_cont_Deg_winner = pickle.load(fileObject)
fileObject.close()

fig = plt.figure(figsize=(20, 7))
fig.suptitle('Accounting Mechanism: Deg \n Allocation Policy: Winner \n     \n    ', fontsize=15)
plt.get_current_fig_manager().window.wm_geometry("+0+0")

plt.subplot(2, 2, 1)
plt.hist(data_cons_data_cont_Deg_winner[0].values(), bins=100, stacked=True, label="Data Consumed")
plt.title("Data Consumed and Contributed (Histogramme)")
plt.hist(data_cons_data_cont_Deg_winner[1].values(), bins=100, stacked=True, label="Data Contributed")
plt.legend()

plt.subplot(2, 2, 2)
sns.set_style('whitegrid')
sns.kdeplot(np.array(data_cons_data_cont_Deg_winner[0].values()), bw=0.5, legend="Data Consumed")
sns.kdeplot(np.array(data_cons_data_cont_Deg_winner[1].values()), bw=0.5, legend="Data Contributed")
plt.title("Data Consumed and Contributed (Density Plot)")


plt.subplot(2, 2, 3)
plt.hist([a-b for a, b in zip(data_cons_data_cont_Deg_winner[0].values(), data_cons_data_cont_Deg_winner[1].values())], bins=100, stacked=True)
plt.title("Data Consumed - Data Contributed")


plt.subplot(2, 2, 4)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_Deg_winner[0].values(), data_cons_data_cont_Deg_winner[1].values())]), bw=0.5)
plt.title("Data Consumed - Data Contributed")
plt.show()




file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values Deg Top n (No Distribution)"
fileObject = open(file_name, 'rb')
data_cons_data_cont_Deg_top_n_nodist = pickle.load(fileObject)
fileObject.close()

fig = plt.figure(figsize=(20, 7))
fig.suptitle('Accounting Mechanism: Deg \n Allocation Policy: Top 4 (No Distribution) \n     \n    ', fontsize=15)
plt.get_current_fig_manager().window.wm_geometry("+0+0")

plt.subplot(2, 2, 1)
plt.hist(data_cons_data_cont_Deg_top_n_nodist[0].values(), bins=100, stacked=True, label="Data Consumed")
plt.title("Data Consumed and Contributed (Histogramme)")
plt.hist(data_cons_data_cont_Deg_top_n_nodist[1].values(), bins=100, stacked=True, label="Data Contributed")
plt.legend()

plt.subplot(2, 2, 2)
sns.set_style('whitegrid')
sns.kdeplot(np.array(data_cons_data_cont_Deg_top_n_nodist[0].values()), bw=0.5, legend="Data Consumed")
sns.kdeplot(np.array(data_cons_data_cont_Deg_top_n_nodist[1].values()), bw=0.5, legend="Data Contributed")
plt.title("Data Consumed and Contributed (Density Plot)")


plt.subplot(2, 2, 3)
plt.hist([a-b for a, b in zip(data_cons_data_cont_Deg_top_n_nodist[0].values(), data_cons_data_cont_Deg_top_n_nodist[1].values())], bins=100, stacked=True)
plt.title("Data Consumed - Data Contributed")


plt.subplot(2, 2, 4)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_Deg_top_n_nodist[0].values(), data_cons_data_cont_Deg_top_n_nodist[1].values())]), bw=0.5)
plt.title("Data Consumed - Data Contributed")
plt.show()




file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values Deg Distribution"
fileObject = open(file_name, 'rb')
data_cons_data_cont_Deg_dist = pickle.load(fileObject)
fileObject.close()

fig = plt.figure(figsize=(20, 7))
fig.suptitle('Accounting Mechanism: Deg \n Allocation Policy: Distribution \n     \n    ', fontsize=15)
plt.get_current_fig_manager().window.wm_geometry("+0+0")

plt.subplot(2, 2, 1)
plt.hist(data_cons_data_cont_Deg_dist[0].values(), bins=100, stacked=True, label="Data Consumed")
plt.title("Data Consumed and Contributed (Histogramme)")
plt.hist(data_cons_data_cont_Deg_dist[1].values(), bins=100, stacked=True, label="Data Contributed")
plt.legend()

plt.subplot(2, 2, 2)
sns.set_style('whitegrid')
sns.kdeplot(np.array(data_cons_data_cont_Deg_dist[0].values()), bw=0.5, legend="Data Consumed")
sns.kdeplot(np.array(data_cons_data_cont_Deg_dist[1].values()), bw=0.5, legend="Data Contributed")
plt.title("Data Consumed and Contributed (Density Plot)")


plt.subplot(2, 2, 3)
plt.hist([a-b for a, b in zip(data_cons_data_cont_Deg_dist[0].values(), data_cons_data_cont_Deg_dist[1].values())], bins=100, stacked=True)
plt.title("Data Consumed - Data Contributed")


plt.subplot(2, 2, 4)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_Deg_dist[0].values(), data_cons_data_cont_Deg_dist[1].values())]), bw=0.5)
plt.title("Data Consumed - Data Contributed")
plt.show()





file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values PGR Top n (Distribution)"
fileObject = open(file_name, 'rb')
data_cons_data_cont_PGR_top_n_dist = pickle.load(fileObject)
fileObject.close()

fig = plt.figure(figsize=(20, 7))
fig.suptitle('Accounting Mechanism: PGR \n Allocation Policy: Top 4 (Distribution) \n     \n    ', fontsize=15)
plt.get_current_fig_manager().window.wm_geometry("+0+0")

plt.subplot(2, 2, 1)
plt.hist(data_cons_data_cont_PGR_top_n_dist[0].values(), bins=100, stacked=True, label="Data Consumed")
plt.title("Data Consumed and Contributed (Histogramme)")
plt.hist(data_cons_data_cont_PGR_top_n_dist[1].values(), bins=100, stacked=True, label="Data Contributed")
plt.legend()

plt.subplot(2, 2, 2)
sns.set_style('whitegrid')
sns.kdeplot(np.array(data_cons_data_cont_PGR_top_n_dist[0].values()), bw=0.5, legend="Data Consumed")
sns.kdeplot(np.array(data_cons_data_cont_PGR_top_n_dist[1].values()), bw=0.5, legend="Data Contributed")
plt.title("Data Consumed and Contributed (Density Plot)")


plt.subplot(2, 2, 3)
plt.hist([a-b for a, b in zip(data_cons_data_cont_PGR_top_n_dist[0].values(), data_cons_data_cont_PGR_top_n_dist[1].values())], bins=100, stacked=True)
plt.title("Data Consumed - Data Contributed")


plt.subplot(2, 2, 4)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_PGR_top_n_dist[0].values(), data_cons_data_cont_PGR_top_n_dist[1].values())]), bw=0.5)
plt.title("Data Consumed - Data Contributed")
plt.show()




file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values PGR, Winner"
fileObject = open(file_name, 'rb')
data_cons_data_cont_PGR_winner = pickle.load(fileObject)
fileObject.close()

fig = plt.figure(figsize=(20, 7))
fig.suptitle('Accounting Mechanism: PGR \n Allocation Policy: Winner \n     \n    ', fontsize=15)
plt.get_current_fig_manager().window.wm_geometry("+0+0")

plt.subplot(2, 2, 1)
plt.hist(data_cons_data_cont_PGR_winner[0].values(), bins=100, stacked=True, label="Data Consumed")
plt.title("Data Consumed and Contributed (Histogramme)")
plt.hist(data_cons_data_cont_PGR_winner[1].values(), bins=100, stacked=True, label="Data Contributed")
plt.legend()

plt.subplot(2, 2, 2)
sns.set_style('whitegrid')
sns.kdeplot(np.array(data_cons_data_cont_PGR_winner[0].values()), bw=0.5, legend="Data Consumed")
sns.kdeplot(np.array(data_cons_data_cont_PGR_winner[1].values()), bw=0.5, legend="Data Contributed")
plt.title("Data Consumed and Contributed (Density Plot)")


plt.subplot(2, 2, 3)
plt.hist([a-b for a, b in zip(data_cons_data_cont_PGR_winner[0].values(), data_cons_data_cont_PGR_winner[1].values())], bins=100, stacked=True)
plt.title("Data Consumed - Data Contributed")


plt.subplot(2, 2, 4)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_PGR_winner[0].values(), data_cons_data_cont_PGR_winner[1].values())]), bw=0.5)
plt.title("Data Consumed - Data Contributed")
plt.show()




file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values PGR Top n (No Distribution)"
fileObject = open(file_name, 'rb')
data_cons_data_cont_PGR_top_n_nodist = pickle.load(fileObject)
fileObject.close()

fig = plt.figure(figsize=(20, 7))
fig.suptitle('Accounting Mechanism: PGR \n Allocation Policy: Top 4 (No Distribution) \n     \n    ', fontsize=15)
plt.get_current_fig_manager().window.wm_geometry("+0+0")

plt.subplot(2, 2, 1)
plt.hist(data_cons_data_cont_PGR_top_n_nodist[0].values(), bins=100, stacked=True, label="Data Consumed")
plt.title("Data Consumed and Contributed (Histogramme)")
plt.hist(data_cons_data_cont_PGR_top_n_nodist[1].values(), bins=100, stacked=True, label="Data Contributed")
plt.legend()

plt.subplot(2, 2, 2)
sns.set_style('whitegrid')
sns.kdeplot(np.array(data_cons_data_cont_PGR_top_n_nodist[0].values()), bw=0.5, legend="Data Consumed")
sns.kdeplot(np.array(data_cons_data_cont_PGR_top_n_nodist[1].values()), bw=0.5, legend="Data Contributed")
plt.title("Data Consumed and Contributed (Density Plot)")


plt.subplot(2, 2, 3)
plt.hist([a-b for a, b in zip(data_cons_data_cont_PGR_top_n_nodist[0].values(), data_cons_data_cont_PGR_top_n_nodist[1].values())], bins=100, stacked=True)
plt.title("Data Consumed - Data Contributed")


plt.subplot(2, 2, 4)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_PGR_top_n_nodist[0].values(), data_cons_data_cont_PGR_top_n_nodist[1].values())]), bw=0.5)
plt.title("Data Consumed - Data Contributed")
plt.show()




file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values PGR Distribution"
fileObject = open(file_name, 'rb')
data_cons_data_cont_PGR_dist = pickle.load(fileObject)
fileObject.close()

fig = plt.figure(figsize=(20, 7))
fig.suptitle('Accounting Mechanism: PGR \n Allocation Policy: Distribution \n     \n    ', fontsize=15)
plt.get_current_fig_manager().window.wm_geometry("+0+0")

plt.subplot(2, 2, 1)
plt.hist(data_cons_data_cont_PGR_dist[0].values(), bins=100, stacked=True, label="Data Consumed")
plt.title("Data Consumed and Contributed (Histogramme)")
plt.hist(data_cons_data_cont_PGR_dist[1].values(), bins=100, stacked=True, label="Data Contributed")
plt.legend()

plt.subplot(2, 2, 2)
sns.set_style('whitegrid')
sns.kdeplot(np.array(data_cons_data_cont_PGR_dist[0].values()), bw=0.5, legend="Data Consumed")
sns.kdeplot(np.array(data_cons_data_cont_PGR_dist[1].values()), bw=0.5, legend="Data Contributed")
plt.title("Data Consumed and Contributed (Density Plot)")


plt.subplot(2, 2, 3)
plt.hist([a-b for a, b in zip(data_cons_data_cont_PGR_dist[0].values(), data_cons_data_cont_PGR_dist[1].values())], bins=100, stacked=True)
plt.title("Data Consumed - Data Contributed")


plt.subplot(2, 2, 4)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_PGR_dist[0].values(), data_cons_data_cont_PGR_dist[1].values())]), bw=0.5)
plt.title("Data Consumed - Data Contributed")
plt.show()
"""


