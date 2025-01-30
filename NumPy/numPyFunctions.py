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

