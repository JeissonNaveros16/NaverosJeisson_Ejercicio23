import os
import numpy as np
import matplotlib.pyplot as plt


a = os.system("c++ walk.cpp -o walk.x")
a = os.system("./walk.x > walk.dat")

plt.figure()
data = np.loadtxt("walk.dat")
plt.plot(data[:,0], data[:,1])
plt.axis('square')
plt.xlim([-50, 50])
plt.ylim([-50, 100])
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig("walk.png")
