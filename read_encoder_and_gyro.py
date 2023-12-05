import time
from machine import Pin
from pololu_3pi_2040_robot import robot
from machine import Pin, UART

turn_rate = 0.0     # degrees per second
robot_angle = 0.0   # degrees
target_angle = 0.0


display = robot.Display()
motors = robot.Motors()
encoders = robot.Encoders()
imu = robot.IMU()
imu.reset()
imu.enable_default()
global last_time_gyro_reading
last_time_gyro_reading = time.ticks_us()
while True:
    uart = UART(0, 115200, tx=Pin(28), rx=Pin(29), stop = 1, timeout = 10) 

    display.fill_rect(40, 48, 64, 16, 0)
    left_encoder, right_encoder = encoders.get_counts()
    display.text(f"{left_encoder:>8}", 30, 48)
    display.text(f"{right_encoder:>8}", 30, 56)

    # Update the angle and the turn rate.
    if imu.gyro.data_ready():
        imu.gyro.read()
        turn_rate = imu.gyro.last_reading_dps[2]  # degrees per second
        now = time.ticks_us()
        if last_time_gyro_reading:
            dt = time.ticks_diff(now, last_time_gyro_reading)
            robot_angle += turn_rate * dt / 1000000
        last_time_gyro_reading = now

    display.fill_rect(48, 32, 72, 8, 0)
    display.text(f"{robot_angle - target_angle:>9.3f}", 48, 32, 1)
    display.show()
