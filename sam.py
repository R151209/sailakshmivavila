import matplotlib.pyplot as plt
import numpy as np
f1=input("enter f1 value:")
f2=input("enter f2 value:")
fs=input("enter fs value:")
n=input("enter no.of samples:")
t=np.arange(n)
x1=np.sin(2*np.pi*f1/fs*t)
plt.subplot(3,1,1)
plt.plot(t,x1)
plt.title('sin sampling')
plt.xlabel('samples')
plt.ylabel('amp')
x2=np.cos(2*np.pi*f2/fs*t)
plt.subplot(3,1,2)
plt.plot(t,x2)
plt.title('cos sampling')
x=x1+x2
plt.subplot(3,1,3)
plt.plot(t,x)
plt.title('sum of two waves')
plt.show( )

