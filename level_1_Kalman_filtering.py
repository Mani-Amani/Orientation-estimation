#this is just a test of the kalman dilter which works decently, the next steps are adding a taylor expansion to implement an EKF and defining the kalman gain as a function of time
import time
import getopt, sys
import math
# import rcpy library
# This automatically initizalizes the robotics cape
import rcpy 
import rcpy.mpu9250 as mpu9250
import numpy

def Kalman(U,r):
   
    h=1
    q=10
    p=10
    u_hat=0
    k=0
    k=p*h/(h*p*(h+r))
    u_hat=u_hat+k+k*(U-h*u_hat)
    p=(1-k*h)*p+q
    return(u_hat)
rcpy.set_state(rcpy.RUNNING)
mpu9250.initialize(enable_magnetometer = True)

print("Press Ctrl-C to exit")

# header
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
            time.sleep(0.01)
        for i in range(0,len(save)):
           sigma=sigma+((save[i]-avg)**2)
           stdv=math.sqrt(sigma/100)    
           cov=stdv**2        
        if rcpy.get_state() == rcpy.RUNNING:
            temp = mpu9250.read_imu_temp()
            data = mpu9250.read_accel_data()


        
        g=Kalman(data[1],cov)
        print(g)
        time.sleep(0.01)  # sleep some
except KeyboardInterrupt:
    # Catch Ctrl-C
    pass

finally:
    print("\nBye BeagleBone!")
