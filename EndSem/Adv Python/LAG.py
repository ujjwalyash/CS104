'''
Lab 7: ADVANCED PYTHON
Activity 1 : LISAN-AL-GAIB (Dune Reference)
Author : Sabyasachi Samantaray

Here we will be dealing only with 2D data to aid visualisation

In this activity, your aim will be the following.
1) Implement the kmeans algorithm completely and correctly.
2) Implement all TODOs without using any loops
'''

### TODO 1: Importing the necessary libraries - numpy, matplotlib and time
### This TODO is already done
import time # to time the execution
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
### TODO 1

### TODO 2
### Load data from data_path
### Check the input file spice_locations.txt to understand the Data Format
### Return : np array of size Nx2
def load_data(data_path):
    return np.loadtxt(data_path, delimiter=',')

### TODO 3.1
### If init_centers is None, initialize the centers by selecting K data points at random without replacement
### Else, use the centers provided in init_centers
### Return : np array of size Kx2
def initialise_centers(data, K, init_centers=None):
    N = data.shape[0]
    centers = init_centers if init_centers else data[np.random.choice(range(1,N), replace=False, size=K)]
    return centers

### TODO 3.2
### Initialize the labels to all ones to size (N,) where N is the number of data points
### Return : np array of size N
def initialise_labels(data):
    N = data.shape[0]
    return np.ones(N, dtype=int)

### TODO 4.1 : E step
### For Each data point, find the distance to each center
### Return : np array of size NxK
def calculate_distances(data, centers):
    data = data.reshape((data.shape[0], 1, data.shape[1]))
    centers = centers.reshape((1, centers.shape[0], centers.shape[1]))
    delta = np.square(data - centers)
    distances = np.sum(delta, axis=2)
    return distances

### TODO 4.2 : E step
### For Each data point, assign the label of the nearest center
### Return : np array of size N
def update_labels(distances):
    labels = np.argmin(distances, axis=1)
    return labels

### TODO 5 : M step
### Update the centers to the mean of the data points assigned to it
### Return : np array of size Kx2
def update_centers(data, labels, K):
    centers = None
    ### IDEA_1
    # sums = np.zeros(shape=(K, data.shape[1]))
    # np.add.at(sums, labels, data)
    # counts = np.zeros(shape=(K, 1))
    # np.add.at(counts, labels, np.ones(shape=(labels.shape[0], 1)))
    # centers = sums/counts

    ### IDEA_2
    # N = data.shape[0]
    # onehot = np.zeros(shape=(K, N), dtype=np.int8)
    # onehot[labels, np.arange(N)] = 1
    # centers = (onehot@data)/(np.sum(onehot, axis=1)).reshape(K, 1)

    ### IDEA_3
    centers_x = np.bincount(labels, data[:, 0])/np.bincount(labels)
    centers_y = np.bincount(labels, data[:, 1])/np.bincount(labels)
    centers = np.vstack((centers_x, centers_y)).T

    return centers

### TODO 6 : Check convergence
### Check if the labels have changed from the previous iteration
### Return : True / False
def check_termination(labels1, labels2):
    return np.array_equal(labels1, labels2)

### DON'T CHANGE ANYTHING IN THE FOLLOWING FUNCTION
def kmeans(data_path:str, K:int, init_centers=None):
    '''
    Input :
        data (type str): path to the file containing the data
        K (type int): number of clusters
        init_centers (type numpy.ndarray): initial centers. shape = (K, 2) or None
    Output :
        centers (type numpy.ndarray): final centers. shape = (K, 2)
        labels (type numpy.ndarray): label of each data point. shape = (N,)
        time (type float): time taken by the algorithm to converge in seconds
    N is the number of data points each of shape (2,)
    '''
    data = load_data(data_path)
    centers = initialise_centers(data, K, init_centers)
    labels = initialise_labels(data)

    start_time = time.time() # Time stamp 

    while True:
        distances = calculate_distances(data, centers)
        labels_new = update_labels(distances)
        centers = update_centers(data, labels_new, K)
        if check_termination(labels, labels_new): break
        else: labels = labels_new
 
    end_time = time.time() # Time stamp after the algorithm ends
    np.savetxt("final.txt", np.hstack((data, labels[:, np.newaxis])), delimiter=",")
    return centers, labels, end_time - start_time

### FILL THE LINES BELOW THE TODO COMMENTS
def visualise(data_path, labels, centers):
    data = load_data(data_path)

    # Scatter plot of the data points
    plt.scatter(data[:, 0], data[:, 1], c=labels, s=50, cmap='viridis')
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)

    ### TODO 7 : In conclusion
    ### Set title as 'K-means clustering'
    plt.title("K-means clustering")
    ### Set xlabel as 'Longitude'
    plt.xlabel('Longitude')
    ### Set ylabel as 'Latitude'
    plt.ylabel('Latitude')
    ### Save the plot as 'kmeans.png'
    plt.savefig('kmeans.png')
    plt.show()
    ## DO NOT CHANGE THE FOLLOWING LINE
    return plt
