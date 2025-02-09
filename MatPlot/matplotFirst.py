import matplotlib as mpl
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd


age = [25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45]
height = [168, 134, 210, 174, 176, 188, 180, 150, 184, 121, 188]

np_age = np.array(age)
np_height = np.array(height)

plt.xlabel('Age')
plt.ylabel('Height')
plt.title('Age vs Height')
plt.plot(np_age, np_height,"g") # g is for green color
plt.show()



