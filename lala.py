import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values 0s Top n (Distribution)"
fileObject = open(file_name, 'rb')
data_cons_data_cont_0s_top_n_dist = pickle.load(fileObject)
fileObject.close()

file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values 0s, Winner"
fileObject = open(file_name, 'rb')
data_cons_data_cont_0s_winner = pickle.load(fileObject)
fileObject.close()

file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values 0s Top n (No Distribution)"
fileObject = open(file_name, 'rb')
data_cons_data_cont_0s_top_n_nodist = pickle.load(fileObject)
fileObject.close()

file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values 0s Distribution"
fileObject = open(file_name, 'rb')
data_cons_data_cont_0s_dist = pickle.load(fileObject)
fileObject.close()

file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values Deg Top n (Distribution)"
fileObject = open(file_name, 'rb')
data_cons_data_cont_Deg_top_n_dist = pickle.load(fileObject)
fileObject.close()

file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values Deg, Winner"
fileObject = open(file_name, 'rb')
data_cons_data_cont_Deg_winner = pickle.load(fileObject)
fileObject.close()

file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values Deg Top n (No Distribution)"
fileObject = open(file_name, 'rb')
data_cons_data_cont_Deg_top_n_nodist = pickle.load(fileObject)
fileObject.close()

file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values Deg Distribution"
fileObject = open(file_name, 'rb')
data_cons_data_cont_Deg_dist = pickle.load(fileObject)
fileObject.close()

file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values PGR Top n (Distribution)"
fileObject = open(file_name, 'rb')
data_cons_data_cont_PGR_top_n_dist = pickle.load(fileObject)
fileObject.close()

file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values PGR, Winner"
fileObject = open(file_name, 'rb')
data_cons_data_cont_PGR_winner = pickle.load(fileObject)
fileObject.close()

file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values PGR Top n (No Distribution)"
fileObject = open(file_name, 'rb')
data_cons_data_cont_PGR_top_n_nodist = pickle.load(fileObject)
fileObject.close()

file_name = "C:\\Users\\alexa\\PycharmProjects\\Community Detection for Sybil Attacks\\Simulation Values PGR Distribution"
fileObject = open(file_name, 'rb')
data_cons_data_cont_PGR_dist = pickle.load(fileObject)
fileObject.close()




fig = plt.figure(figsize=(20, 7))
plt.get_current_fig_manager().window.wm_geometry("+0+0")


plt.subplot(3, 4, 1)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_0s_top_n_dist[0].values(), data_cons_data_cont_0s_top_n_dist[1].values())]), bw=0.5)
plt.title("0s top 4 (Dist)")

plt.subplot(3, 4, 2)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_0s_winner[0].values(), data_cons_data_cont_0s_winner[1].values())]), bw=0.5)
plt.title("0s Winner")

plt.subplot(3, 4, 3)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_0s_top_n_nodist[0].values(), data_cons_data_cont_0s_top_n_nodist[1].values())]), bw=0.5)
plt.title("0s top 4 (No Dist)")

plt.subplot(3, 4, 4)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_0s_dist[0].values(), data_cons_data_cont_0s_dist[1].values())]), bw=0.5)
plt.title("0s Dist")

plt.subplot(3, 4, 5)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_Deg_top_n_dist[0].values(), data_cons_data_cont_Deg_top_n_dist[1].values())]), bw=0.5)


plt.subplot(3, 4, 6)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_Deg_winner[0].values(), data_cons_data_cont_Deg_winner[1].values())]), bw=0.5)


plt.subplot(3, 4, 7)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_Deg_top_n_nodist[0].values(), data_cons_data_cont_Deg_top_n_nodist[1].values())]), bw=0.5)


plt.subplot(3, 4, 8)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_Deg_dist[0].values(), data_cons_data_cont_Deg_dist[1].values())]), bw=0.5)


plt.subplot(3, 4, 9)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_PGR_top_n_dist[0].values(), data_cons_data_cont_PGR_top_n_dist[1].values())]), bw=0.5)


plt.subplot(3, 4, 10)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_PGR_winner[0].values(), data_cons_data_cont_PGR_winner[1].values())]), bw=0.5)


plt.subplot(3, 4, 11)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_PGR_top_n_nodist[0].values(), data_cons_data_cont_PGR_top_n_nodist[1].values())]), bw=0.5)


plt.subplot(3, 4, 12)
sns.set_style('whitegrid')
sns.kdeplot(np.array([a-b for a, b in zip(data_cons_data_cont_PGR_dist[0].values(), data_cons_data_cont_PGR_dist[1].values())]), bw=0.5)


plt.show()