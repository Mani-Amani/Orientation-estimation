import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
import scipy
import numpy as np
import math

def q_mult(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    return w, x, y, z
def Quat(n,alpha):
    x,y,z=n
    n=normalize(n)
    w=math.cos(alpha/2)
    y=y*math.sin(alpha/2)
    x=x*math.sin(alpha/2)
    z=z*math.sin(alpha/2)
    return(w,x,y,z)
def q_conjugate(q):
    w, x, y, z = q
    return (w, -x, -y, -z)
def normalize(v, tolerance=0.0000001):
    mag2 = sum(n * n for n in v)
    if abs(mag2 - 1.0) > tolerance:
        mag = np.sqrt(mag2)
        v = tuple(n / mag for n in v)
    return v
def q_to_axisangle(q):
    w, v = q[0], q[1:]
    theta = acos(w) * 2.0
    return normalize(v), theta
def qv_mult(q1, v1):
    q2 = (0.0,) + v1
    return q_mult(q_mult(q1, q2), q_conjugate(q1))[1:]
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
