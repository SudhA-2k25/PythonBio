# Hierarcical clustering

import pandas as pd
customer_data = pd.read("shopping-data.csv")
customer_data


import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch

selected_data = np.array([[3], [7], [8]])

plt.figure(figsize=(10, 7))
plt.title("Customers Dendrogram with line")
clusters = sch.linkage(selected_data, method='ward', metric="euclidean")
sch.dendrogram(clusters)
plt.axhline(y=3, color='r', linestyle='-')
plt.show()
