import csv  
import pandas as pd
import matplotlib.pyplot as plt  
andro_movelist = pd.read_csv("data.csv")  
andro_movelist.head()  
andro_movelist['LIGHT'].value_counts().plot(kind='bar')  
plt.ylabel('Count')  
plt.savefig("test.png")  
plt.show()  
