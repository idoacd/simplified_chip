import tensorflow as tf
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np


xx=tf.random_uniform([20,2])*5-2.5
xx=tf.Session().run(xx)

#yy = xx[:,0] * 2 + xx[:,1] * 3 + 400


fig = plt.figure()
ax = fig.gca(projection='3d')
X = xx[:,0]
Y = xx[:,1]
X, Y = np.meshgrid(X, Y)
#R = np.sqrt(X**2 + Y**2)
#Z = np.sin(.5*R)
Z=np.array(-X*1.8+Y*0.8+2)
#Z[(X+Y<2) & (Y-X>-2) & (-X+Y<2) & (Y+X>-2)] = np.nan  # the diagonal slice
Z[(X<1) & (X>-1) & (Y<1) & (Y>-1)]=np.nan
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False, vmin=-5, vmax=5)
ax.set_zlim(-6.01, 6.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.01f'))


fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()