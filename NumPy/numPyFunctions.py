import numpy as np

my_list = [10,20,30,40,50] #python list variable

my_array = np.array(my_list)  #list variable convert to numpy array type

print(type(my_list)) # : <class 'list'>
print(type(my_array)) # : <class 'numpy.ndarray'>

print(my_array) # : [10 20 30 40 50]
print(my_array[0]) # : 10
print(my_array[-2]) # : 40

my_array[1] = 200
print(my_array) # : [ 10 200  30  40  50]

print(my_array.max()) # : 200 maximum value
print(my_array.min()) # : 10 minimum value
print(my_array.mean()) # : 66.0 average value

list_python = [[1,0,0],[0,1,0],[0,0,1],[0,0,0]] # python list variable
print(list_python[1][1]) # : 1

## Np Matrix
np_matrix = np.array(list_python) # NumPy matrix variable
print(np_matrix) # :
                     # [1 0 0]
                     # [0 1 0]
                     # [0 0 1]
                     # [0 0 0]

print(np_matrix[0]) # : [1,0,0]
print(np_matrix[0][0]) # : 1

print(np_matrix.shape) # : (4,3)  array size 4-rows and 3-columns

## Arrange ##
new_matrix = np.arange(0,10) # : [0 1 2 3 4 5 6 7 8 9]
new_matrix = np.arange(0,100,10) # : [ 0 10 20 30 40 50 60 70 80 90]
print(new_matrix)

print(np.zeros((3,3)))
                        # : [0. 0. 0.]
                        #   [0. 0. 0.]
                        #   [0. 0. 0.]
print(np.ones((4,3)))
                        #: [1. 1. 1. 1.]
                        #  [1. 1. 1. 1.]
                        #  [1. 1. 1. 1.]
                        #  [1. 1. 1. 1.]

## linspace:
print(np.linspace(0,10,10))
            # [ 0.          1.11111111  2.22222222  3.33333333  4.44444444  5.55555556
            #   6.66666667  7.77777778  8.88888889 10.        ]

## random:
print(np.random.randint(1,100,5)) # : [75 82 83 26 56] 1 to 100 random 5 numbers