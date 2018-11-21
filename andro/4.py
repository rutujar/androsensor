from numpy import genfromtxt  
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
data = np.genfromtxt('defaultdata.csv', delimiter=',', names=['LIGHT', 'GRAVY'])  
plt.plot(data['LIGHT'], data['GRAVY'])  
plt.show() 
