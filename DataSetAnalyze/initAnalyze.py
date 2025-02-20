import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
##import seaborn as sns
import matplotlib as mpl

data_file = 'train.csv'

dataset = pd.read_csv(data_file)

print(dataset.head())