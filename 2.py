import statistics  
import pandas as pd  
import matplotlib.pyplot as plt  
	  
	  
DATA = pd.read_csv('defaultdata.csv', sep=',')  
  
X_AXIS = DATA['ACCEX']  
Y_AXIS = DATA['ACCEY']  
Z_AXIS = DATA['ACCEZ']  
	  
light = DATA['GRAVX']  
	  
plt.axhline(y=0)  
	  
	  
plt.axvline(x=0)  
	  
plt.plot(light, X_AXIS, 'r', light, Y_AXIS, 'g', light, Z_AXIS, 'b')  
plt.minorticks_on()  
plt.legend((' = ACCEX', ' = ACCEY', ' = ACCEZ'))  
plt.show()  
# Print out Sensors  
MINX = min(X_AXIS)  
MAXX = max(X_AXIS)  
AVGX = statistics.mean(X_AXIS)  
	  
MINY = min(Y_AXIS)  
MAXY = max(Y_AXIS)  
AVGY = statistics.mean(Y_AXIS)  
	  
MINZ = min(Z_AXIS)  
MAXZ = max(Z_AXIS)  
AVGZ = statistics.mean(Z_AXIS)  
	  
print('\n-----------------------------------')  
print('The min of the X Axis is %s.' % MINX)  
print('The max of the X Axis is %s.' % MAXX)  
print('The average of the X Axis is %.2f.' % AVGX)  
	  
print('\nThe min of the Y Axis is %s.' % MINY)  
print('The max of the Y Axis is %s.' % MAXY)  
print('The average of the Y Axis is %.2f.' % AVGY)  
	  
print('\nThe min of the Z Axis is %s.' % MINZ)  
print('The max of the Z Axis is %s.' % MAXZ)  
print('The average of the Z Axis is %.2f.' % AVGZ)  
	  
SECONDS = light / 100  
MINSEC = float(min(SECONDS))  
MAXSEC = float(max(SECONDS))  
	  
print('The min time is %.2f' % MINSEC)  
print('The max time is %.2f' % MAXSEC)  
