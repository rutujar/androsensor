import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sf = pd.read_csv('data.csv')
sf.head()
sf.drop(sf.columns[[0, 2, 3, 15, 17, 18]], axis=1, inplace=True)
sf.info()
sf.hist(bins=50, figsize=(20,15))
plt.savefig("attribute_histogram_plots")
plt.show()
sf.plot(kind="scatter", x="LOCAL", y="LOCAT", alpha=0.2)
plt.savefig('map1.png')
sf.plot(kind="scatter", x="LOCAL", y="LOCAT", alpha=0.4, figsize=(10,5), c="ACCEY", cmap=plt.get_cmap("jet"), colorbar=True, sharex=False)
from pandas.tools.plotting import scatter_matrix
attributes = ["LOCAL", "LIGHT", "PROX", "LACCX"]
scatter_matrix(sf[attributes], figsize=(12, 8))
plt.savefig('matrix.png')
