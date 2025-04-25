from LAG import *
import numpy as np
# raw = np.loadtxt("final.txt", delimiter=",")
# labels = raw[:, 2].astype(int)

def LAG_score(data, centers):
    data = data.reshape((data.shape[0], 1, data.shape[1]))
    centers = centers.reshape((1, centers.shape[0], centers.shape[1]))
    delta = np.square(data - centers)
    distances = np.sqrt(np.sum(delta, axis=2))
    return np.sum(np.min(distances, axis=1))
def mean_intra_cluster_distence(data, labels):
    mat = (labels == labels[:, np.newaxis])
    dist = np.sqrt(np.sum(np.square((data[:, np.newaxis, :] - data[np.newaxis, :, :])), axis=2))
    distsum = np.sum(dist, 0, where=mat)
    counts = np.sum(np.ones(dist.shape), 0, where=mat) - 1
    # np.apply_along_axis(lambda point : 0 if (np.sum(np.ones(labels.shape), where=(labels == labels[point[0]])) - 1) == 0 else np.sum(np.sqrt((np.square(data - data[point[0]])[:, 0] + np.square(data - data[point[0]])[:, 1])),where=(labels == labels[point[0]]))/(np.sum(np.ones(labels.shape), where=(labels == labels[point[0]])) - 1) , 1, arr=np.arange(data.shape[0])[:, np.newaxis])
    return distsum/counts

def mean_neighbour_cluster_distence(data, labels, centers):
    newdata = data.reshape((data.shape[0], 1, data.shape[1]))
    centers = centers.reshape((1, centers.shape[0], centers.shape[1]))
    delta = np.square(newdata - centers)
    distances = np.sqrt(np.sum(delta, axis=2))
    nearest = np.argsort(distances)[:, 1]
    
    mat = (nearest == labels[:, np.newaxis])
    dist = np.sqrt(np.sum(np.square((data[:, np.newaxis, :] - data[np.newaxis, :, :])), axis=2))
    distsum = np.sum(dist, 0, where=mat)
    counts = np.sum(np.ones(dist.shape), 0, where=mat)

    # np.apply_along_axis(lambda point: np.sum(np.sqrt(np.square(data - data[point])[:, 0] + np.square(data - data[point])[:, 1]), where=(labels == nearest[point])) , 1, arr=np.arange(data.shape[0])[:, np.newaxis]))
    return distsum/counts

def sil_score(data, labels, centers):
    a = mean_intra_cluster_distence(data, labels)
    b = mean_neighbour_cluster_distence(data, labels, centers)
    return np.mean((b-a)/np.maximum(a,b))

def generate_plot(data_path, K_max):
    data = np.loadtxt(data_path, delimiter=",")
    lag_scores = []
    sil_scores = []
    for i in range(2,1+K_max):
        centers, labels, exectime = kmeans(data_path, i)
        micd = mean_intra_cluster_distence(data, labels)
        lag_scores.append(LAG_score(data, centers))
        sil_scores.append(sil_score(data, labels, centers))
        plt.hist(micd, label=f"K = {i}", color=(f'C{i}', 0.5))
    plt.ylabel("Frequencies")
    plt.xlabel("Mean intra cluster distence")
    plt.legend()
    plt.show()

    plt.plot(range(2, 1+K_max), lag_scores, label="LAG")
    plt.legend()
    plt.show()

    plt.plot(range(2, 1+K_max), sil_scores, label="SIL")
    plt.legend()
    plt.show()

generate_plot("spice_locations.txt", 6)