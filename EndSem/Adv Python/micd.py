from LAG import *
import numpy as np
raw = np.loadtxt("final.txt", delimiter=",")
data = raw[:, [0, 1]]
labels = raw[:, 2].astype(int)

def mean_intra_cluster_distence(data, labels):
    return np.apply_along_axis(lambda point : 0 if (np.sum(np.ones(labels.shape), where=(labels == labels[point])) - 1) == 0 else np.sqrt(np.sum(np.square(np.sum(data - data[point], 0, where=(labels == labels[point])[:, np.newaxis]))))/(np.sum(np.ones(labels.shape), where=(labels == labels[point])) - 1) , 1, arr=np.arange(data.shape[0])[:, np.newaxis])
    

def generate_plot(data_path, K_max):
    data = np.loadtxt(data_path, delimiter=",")
    for i in range(2,1+K_max):
        centers, labels, exectime = kmeans(data_path, i)
        micd = mean_intra_cluster_distence(data, labels)
        plt.hist(micd, label=f"K = {i}", color=(f'C{i}', 0.5))
    plt.ylabel("Frequencies")
    plt.xlabel("Mean intra cluster distence")
    plt.legend()
    plt.show()

generate_plot("spice_locations.txt", 6)

        
