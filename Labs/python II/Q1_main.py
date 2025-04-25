'''
The Matrix
--------------------------------------------------------------------------
Some helpful References:
1. statistics
https://numpy.org/doc/stable/reference/routines.statistics.html

2. matrix operations
https://towardsdatascience.com/top-10-matrix-operations-in-numpy-with-examples-d761448cb7a8

3. padding
https://numpy.org/doc/stable/reference/generated/numpy.pad.html

--------------------------------------------------------------------------
A young programmer named Python yearned for freedom. He dreamed of breaking through the simulated reality that bound humanity, but the path was fraught with challenges.
Python knew that to unravel the Matrix, he needed speed and precision in his computations. Struggling with the limitations of his native tools, he turned to NumPy, a powerful ally renowned for its lightning-fast array operations. With the help of NumPy, Python successfully could escape "The Matrix".
Let's see if you can do it too!
You are given a numpy array. You need to perform various operations on it, as detailed below.

The given matrix:
5,5,84,3,9
6,11,1,55,58
1,20,48,12,36
8,4,41,93,98
6,17,64,0,13

All expected outputs are given for this input matrix. Do not hardcode the outputs, otherwise they will fail for almost all other matrices!

Task 1:
Return the transpose of the upper triangular matrix including the diagonal of the input matrix

Testing:
(Uncomment the code in the main function corresponding to testing of task 1)
>> print(task1(matrix))
'''

'''
    NumPy and The Matrix
'''

import numpy as np

def task1(matrix):
    '''return the upper diagonal matrix in column-wise fashion'''
    return np.triu(matrix).T

def task2(matrix):
    '''return mean, median, std (precision 2), all along x, determinant, inverse, pseudo-inverse'''
    mean = np.mean(matrix, axis=0)
    median = np.median(matrix, axis=0)
    std = np.std(matrix, axis=0)
    det = np.linalg.det(matrix)
    inv = np.linalg.inv(matrix)
    pseudoinv = np.linalg.pinv(matrix)
    return mean, median, std, det, inv, pseudoinv

def task3(matrix, num = 0, padding = 3):
    '''return the padded matrix'''
    return np.pad(matrix, pad_width=padding, mode="constant", constant_values=num)

if __name__ == '__main__':

    matrix = np.array([
        [5,5,84,3,9],
        [6,11,1,55,58],
        [1,20,48,12,36],
        [8,4,41,93,98],
        [6,17,64,0,13]
    ])

    # you can call the functions here
    # Uncomment the following lines to test your code

    # TASK 1
    # print(task1(matrix))

    # TASK 2
    # mean, median, std, det, inv, pseudoinv = task2(matrix)
    # print("Mean: ", mean)
    # print("Median: ", median)
    # print("Standard Deviation: ", std)
    # print("Determinant: ", det)
    # print("Inverse: ", inv)
    # print("Pseudo-Inverse: ", pseudoinv)

    # TASK 3
    # print(task3(matrix)) # default padding