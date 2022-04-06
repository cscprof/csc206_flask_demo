# From - https://stackabuse.com/generating-synthetic-data-with-numpy-and-scikit-learn/

import numpy as np

# Needed for plotting
import matplotlib.colors
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Needed for generating classification, regression and clustering datasets
import sklearn.datasets as dt

# Needed for generating data from an existing dataset
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV

# Define the seed so that results can be reproduced
seed = 11
rand_state = 11

# Define the color maps for plots
color_map = plt.cm.get_cmap('RdYlBu')
color_map_discrete = matplotlib.colors.LinearSegmentedColormap.from_list("", ["red","cyan","magenta","blue"])

fig = plt.figure(figsize=(18,5))

x,y = dt.make_friedman1(n_samples=1000,n_features=5,random_state=rand_state)
ax = fig.add_subplot(131, projection='3d')
my_scatter_plot = ax.scatter(x[:,0], x[:,1],x[:,2], c=y, cmap=color_map)
fig.colorbar(my_scatter_plot)
plt.title('make_friedman1')

x,y = dt.make_friedman2(n_samples=1000,random_state=rand_state)
ax = fig.add_subplot(132, projection='3d')
my_scatter_plot = ax.scatter(x[:,0], x[:,1],x[:,2], c=y, cmap=color_map)
fig.colorbar(my_scatter_plot)
plt.title('make_friedman2')

x,y = dt.make_friedman3(n_samples=1000,random_state=rand_state)
ax = fig.add_subplot(133, projection='3d')
my_scatter_plot = ax.scatter(x[:,0], x[:,1],x[:,2], c=y, cmap=color_map)
fig.colorbar(my_scatter_plot)
plt.suptitle('make_friedman?() for Non-Linear Data',fontsize=20)
plt.title('make_friedman3')

plt.show()