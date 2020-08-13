       if rcpy.get_state() == rcpy.RUNNING:
            temp = mpu9250.read_imu_temp()
            data = mpu9250.read_gyro_data()
            x_cord= data[0]
            y_cord=data[1]
            z_cord=data[2]
            x_for_calc=x_cord-x_calib_avg_2
            if x_for_calc<0.025 and x_for_calc>-0.025:
               x_for_calc=0
            if y_for_calc<0.025 and y_for_calc>-0.025:
               y_for_calc=0
            if z_for_calc<0.025 and z_for_calc>-0.025:
               z_for_calc=0
            time.sleep(0.01)    
       if rcpy.get_state() == rcpy.RUNNING:
            temp = mpu9250.read_imu_temp()
            data = mpu9250.read_gyro_data()
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
        angle_x=(x_for_calc+(x_for_calc-x_for_calc_n2)/2)*0.02
        angle_y=(y_for_calc+(y_for_calc-y_for_calc_n2)/2)*0.02
        angle_z=(z_for_calc+(z_for_calc-z_for_calc_n2)/2)*0.02
    return (angle_x,angle_y,angle_z)    
