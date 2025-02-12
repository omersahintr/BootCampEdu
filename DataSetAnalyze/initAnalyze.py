import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

data_file = "DataSetAnalyze/train.csv"
dataset = pd.read_csv(data_file)


plt.figure(figsize=(18, 10))
sns.heatmap(dataset.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.show()



print(dataset)