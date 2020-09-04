
#this is just a test of the kalman dilter which works decently, the next steps are adding a taylor expansion to implement an EKF and defining the kalman gain as a function of time
import time
import getopt, sys
import math
from sympy import diff
# import rcpy library
# This automatically initizalizes the robotics cape
import rcpy 
import rcpy.mpu9250 as mpu9250
import numpy
rcpy.set_state(rcpy.RUNNING)
mpu9250.initialize(enable_magnetometer = True)
E=[[1,0,0],[0,1,0],[0,0,1]]
X=[[0],[0],[0]]
Q=[[2,0,0],[0,2,0],[0,0,2]]
def Kalman(data_gyro,data_accel,r):
    global X
    global E
    global Q
    X_old=X
    E_old=E
    data_gyro=numpy.transpose(data_gyro)
    data_accel=numpy.transpose(data_accel)
    I=[[1,0,0],[0,1,0],[0,0,1]]
    E_est=numpy.matmul(I,E_old,numpy.transpose(I),casting='unsafe')+Q
    K=numpy.matmul(E_est,numpy.transpose(I),numpy.linalg.inv((E)),casting='unsafe')
    X_est=X_old+data_gyro
    X=X_est+numpy.matmul(K,(data_accel-X_old),casting='unsafe')
    E=E_est-numpy.matmul(K,E_est,casting='unsafe')
    print(E)
    print(E_est)
    print(K)
    return(X)

print("Press Ctrl-C to exit")

# header,,
print("   Accel XYZ (m/s^2) |"
      "    Gyro XYZ (deg/s) |", end='')
print("  Mag Field XYZ (uT) |", end='')
print(' Temp (C)')
i=0
avg=0
save=[]
sigma=0
cov=0

try:    # keep running
    while True:
        while i<100:
            if rcpy.get_state() == rcpy.RUNNING:
                temp = mpu9250.read_imu_temp()
                data = mpu9250.read_accel_data()
                save.append(data[1])
                avg=avg+data[1]
            i=i+1
            avg=avg/100  
            print('doing')
            time.sleep(0.01)
        print('done')
        for i in range(0,len(save)):
           sigma=sigma+((save[i]-avg)**2)
           stdv=math.sqrt(sigma/100)    
           cov=stdv**2        
           cov=[[cov,0,0],[0,cov,0],[0,0,cov]]
        print('done1')
        if rcpy.get_state() == rcpy.RUNNING:
            print('hi')
            temp = mpu9250.read_imu_temp()
            data = mpu9250.read_accel_data()
            data_gyro=mpu9250.read_gyro_data()
            g=Kalman(data,data_gyro,cov)
            print(g)
        time.sleep(1)  # sleep some
except KeyboardInterrupt:
    # Catch Ctrl-C
    pass

finally:
    print("\nBye BeagleBone!")
