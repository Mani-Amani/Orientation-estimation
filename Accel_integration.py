
def accel_distance ():
    try:
        while True:
        #getting state and reading the imu data\
        #we basically repeat the function 4 times in 0.01 second intervals so we have 4 data points so we can integrate twice to get distance from accelaration
            if rcpy.get_state() == rcpy.RUNNING:
                temp = mpu9250.read_imu_temp()
                data = mpu9250.read_accel_data()
        #saving the coordinate data from the tuple
                x_cord= data[0]
                y_cord=data[1]
                z_cord=data[2]
        #decreasing the raw data from average imu noise for more accurate numbers    
                x_for_calc=x_cord-x_calib_avg_2
                z_for_calc=z_for_calc-z_calib_avg_2
                y_for_calc=y_for_calc-y_calib_avg_2
        # further estimation to ignore small instances and vibrations
                if x_for_calc<0.025 and x_for_calc>-0.025:
                    x_for_calc=0
                if z_for_calc<0.025 and z_for_calc>-0.025:
                    z_for_calc=0
                if y_for_calc<0.025 and y_for_calc>-0.025:
                    y_for_calc=0
                time.sleep(0.01)
        #the second data point
            if rcpy.get_state() == rcpy.RUNNING:
                temp = mpu9250.read_imu_temp()
                data = mpu9250.read_accel_data()
                x_cord_n2= data[0]
                y_cord_n2=data[1]
                z_cord_n2=data[2]
                x_for_calc_n2=x_cord_n2-x_calib_avg_2
                if x_for_calc_n2<0.025 and x_for_calc_n2>-0.025:
                    x_for_calc_n2=0
                if y_for_calc_n2<0.025 and y_for_calc_n2>-0.025:
                    y_for_calc_n2=0
                if z_for_calc_n2<0.025 and z_for_calc_n2>-0.025:
                    z_for_calc_n2=0
                time.sleep(0.01)
        #the third datapoint
             if rcpy.get_state() == rcpy.RUNNING:
                temp = mpu9250.read_imu_temp()
                data = mpu9250.read_accel_data()
                x_cord_n3= data[0]
                y_cord_n3=data[1]
                z_cord_n3=data[2]
                x_for_calc_n3=x_cord_n3-x_calib_avg_2
                if x_for_calc_n3<0.025 and x_for_calc_n3>-0.025:
                    x_for_calc_n3=0
                if y_for_calc_n3<0.025 and y_for_calc_n3>-0.025:
                    y_for_calc_n3=0
                if z_for_calc_n3<0.025 and z_for_calc_n3>-0.025:
                    z_for_calc_n3=0    
                time.sleep(0.01)
        #the fourth data point
             if rcpy.get_state() == rcpy.RUNNING:
                 temp = mpu9250.read_imu_temp()
                 data = mpu9250.read_accel_data()
                 x_cord_n4= data[0]
                 y_cord_n4=data[1]
                 z_cord_n4=data[2]
                 x_for_calc_n4=x_cord_n4-x_calib_avg_2
                 y_for_calc_n4=y_cord_n4-y_calib_avg_2
                 z_for_calc_n4=z_cord_n4-z_calib_avg_2
                 if x_for_calc_n4<0.025 and x_for_calc_n4>-0.025:
                     x_for_calc_n4=0
                 if y_for_calc_n4<0.025 and y_for_calc_n4>-0.025:
                     y_for_calc_n4=0
                 if z_for_calc_n4<0.025 and z_for_calc_n4>-0.025:
                     z_for_calc_n4=0    
        #trapezoidal integration to acquire 2 speed datapoints, accel 1,2 for speed 1 and accel 3,4 for speed        
            speed_n1_x= (x_for_calc+(x_for_calc-x_for_calc_n2)/2)*0.01
            speed_n2_x= (x_for_calc_n3+(x_for_calc_n3-x_for_calc_n4)/2)*0.01
            speed_n1_y= (y_for_calc+(y_for_calc-y_for_calc_n2)/2)*0.01
            speed_n2_y= (y_for_calc_n3+(y_for_calc_n3-y_for_calc_n4)/2)*0.01
            speed_n1_z= (z_for_calc+(z_for_calc-z_for_calc_n2)/2)*0.01
            speed_n2_z= (z_for_calc_n3+(y_for_calc_n3-y_for_calc_n4)/2)*0.01
        #integration for distance
            distance_inst_x=(speed_n1_x+(speed_n1_x-speed_n2_x)/2)*0.02
            distance_inst_y=(speed_n1_y+(speed_n1_y-speed_n2_y)/2)*0.02
            distance_inst_z=(speed_n1_z+(speed_n1_z-speed_n2_z)/2)*0.02
        #adding distance to total distance
            distance_total_x=distance_inst_x+distance_total_x
            distance_total_y=distance_inst_y+distance_total_y
            distance_total_z=distance_inst_z+distance_total_z
     except KeyboardInterrupt:
          return(distance_total_x,distance_total_y,distance_total_z)
def angles():
