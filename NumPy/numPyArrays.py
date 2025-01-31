import numpy as np

np_array = np.arange(0,10) # : [0 1 2 3 4 5 6 7 8 9]
print(np_array)

## Slicing
print(np_array[2:6]) # : [2 3 4 5 ]
print(np_array[0:10:2]) # : [0 2 4 6 8]

np_array[2:5] = -1 # : [ 0  1 -1 -1 -1  5  6  7  8  9]
print(np_array)

mid_list = np_array[3:7]
print(mid_list) # : [-1 -1  5  6]

mid_list[:] = 10
print(mid_list) # : [10 10 10 10]
print(np_array) # : [ 0  1 -1 10 10 10 10  7  8  9]

# Slicing Copy Arrays Method
a_array = np.arange(0,10) # : [0 1 2 3 4 5 6 7 8 9] --> [0 1 2 3 4 5 6 7 8 9]
b_array = a_array.copy() # : [0 1 2 3 4 5 6 7 8 9] --> [0 1 2 3 99 99 99 99 99 9]
c_array = b_array[4:9] # : [4 5 6 7 8]
c_array[:] = 99 # : [99 99 99 99 99]

print(f"a_array={a_array}\nb_array={b_array}\nc_array={c_array}")

# Numpy Array Operations

x_array = np.random.randint(1,100,20)
final_array = x_array > 50 # : [ True  True  True  True False False  True False  True  True False False
                    # False False False  True False False False  True]
print(x_array[final_array]) # : >50 listing --> [58 66 56 93 62 67 98 56 77 93 52 61]


end_array = np.arange(1,10)

print(end_array) # : [1 2 3 4 5 6 7 8 9]
print(end_array + end_array) # : [ 2  4  6  8 10 12 14 16 18]
print(end_array - end_array) # : [0 0 0 0 0 0 0 0 0]
print(end_array * end_array) # : [ 1  4  9 16 25 36 49 64 81]
print(end_array / end_array) # : [1. 1. 1. 1. 1. 1. 1. 1. 1.]

this_array = np.arange(1,10)

print(this_array.max()) # : 9
print(np.max(this_array)) # : 9

print(this_array.min()) # : 1
print(this_array.mean()) # : 5.0
print(np.sqrt(this_array[2])) # : 1.7320508075688772

