import matplotlib.pyplot as plt
import numpy as np
t=np.arange(0,10,0.0001)
x1=np.sin(t*2*np.pi)
plt.plot(t,x1)
plt.title('sine wave')
plt.xlabel('time')
plt.ylabel('amp')
plt.show( )