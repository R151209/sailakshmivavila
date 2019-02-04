import matplotlib.pyplot as plt
import numpy as np
t=np.arange(0,10,0.5)
x1=np.sin(2*np.pi*t)
plt.subplot(1,3,1)
plt.stem(t,x1)
plt.title('sine_wave')
plt.xlabel('----->time')
plt.ylabel('----->amp')
x2=np.cos(2*np.pi*t)
plt.subplot(1,3,2)
plt.plot(t,x2)
plt.title('cos_wave')
x=x1+x2
plt.subplot(1,3,3)
plt.plot(t,x)
plt.title('add of sine & cos')
plt.show( )
