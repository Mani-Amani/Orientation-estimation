import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
import scipy
import numpy as np
import math
n = np.array([0,1,0])
def Quat(alpha):
    x,y,z=n
    alpha=alpha/180*math.pi
    w=math.cos(alpha/2)
    y=y*math.sin(alpha/2)
    x=x*math.sin(alpha/2)
    z=z*math.sin(alpha/2)
    return(w,x,y,z)
q=[]
q=Quat(-60)

rt=np.matrix([[((1-2*(q[2]**2))-2*(q[3]**2))  ,  2*(q[1]*q[2]-q[0]*q[3]), 2*(q[1]*q[3]+q[0]*q[2]) ],
            [2*(q[1]*q[2]+q[0]*q[3]), ((1-2*(q[1]**2))-2*(q[3]**2)), 2*(q[2]*q[3]-q[0]*q[1])  ],
            [2*(q[1]*q[3]-q[0]*q[2]), 2*(q[2]*q[3]+q[0]*q[1]),((1-2*(q[1]**2))-2*(q[2]**2)) ]])
vec=[[1],[0],[0]]
print(rt)
rotated=rt*vec
print(rotated)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0,0,0,n[0],n[1],n[2])
ax.quiver(0,0,0,rotated[0],rotated[1],rotated[2],color='green')
ax.quiver(0,0,0,vec[0],vec[1],vec[2],color='red')
ax.set_xlim([1, 0])
ax.set_ylim([1, 0])
ax.set_zlim([0, 1])
