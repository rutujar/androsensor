import csv  
import matplotlib.pyplot as plt  
outfile = open("defaultdata.csv","r")  
 
file=csv.reader(outfile)  
next(file, None)  
  
ACCEX = []  
GRAVX = []  
LACCX = []  
  
for row in file:  
    ACCEX.append(row[0])  
    GRAVX.append(row[1])  
    LACCX.append(row[2])  
	  
plt.pie(LACCX, labels=ACCEX)  
plt.axis('equal')  
plt.savefig("pie.png")# make the pie chart circular  
plt.show() 
