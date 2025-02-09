import matplotlib as mpl
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd


age = [25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45]
height = [168, 134, 210, 174, 176, 188, 180, 150, 184, 121, 188]

np_age = np.array(age) # convert list to numpy array
np_height = np.array(height) # convert list to numpy array

plt.xlabel('Age') # x-axis label
plt.ylabel('Height') # y-axis label
plt.title('Age vs Height') # title of the graph
plt.plot(np_age, np_height,"g") # g is for green color
plt.show() # display the graph




new_numpay1 = np.linspace(0, 10, 20) # 20 numbers between 0 and 10
new_numpay2 = new_numpay1 ** 2 # square of each number in new_numpay1
print(new_numpay2) 

plt.subplot(1, 2, 1) # 1 row, 2 columns, 1st position
plt.plot(new_numpay1, new_numpay2, 'r*-') # r is for red color + is for plus sign
plt.subplot(1, 2, 2) # 1 row, 2 columns, 2nd position
plt.plot(new_numpay2, new_numpay1, 'g+-') # g is for green color -- is for dash line
plt.show() # display the graph



new_numpay11 = np.linspace(0, 10, 20) # 20 numbers between 0 and 10
new_numpay22 = new_numpay11 ** 2 # square of each number in new_numpay1
print(new_numpay22)

figures = plt.figure() # create a figure object
coord = figures.add_axes([0.1, 0.1, 0.8, 0.8]) # add axes to the figure
coord.plot(new_numpay11, new_numpay22, 'b') # b is for blue color
coord.set_xlabel('X-axis') # x-axis label
coord.set_ylabel('Y-axis') # y-axis label
coord.set_title('Max Chart') # title of the graph

coord2 = figures.add_axes([0.2, 0.5, 0.4, 0.3]) # add axes to the figure
coord2.plot(new_numpay22, new_numpay11, 'r') # r is for red color
coord2.set_xlabel('X-axis') # x-axis label
coord2.set_ylabel('Y-axis') # y-axis label
coord2.set_title('Min Chart') # title of the graph

plt.show() # display the graph




