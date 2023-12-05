from pololu_3pi_2040_robot import robot
import time

motors = robot.Motors()
bump_sensors = robot.BumpSensors()
display = robot.Display()

display.fill(0)
display.show()

bump_sensors.calibrate()
time.sleep_ms(1000)

max_speed = 500
turn_time = 5000
motors.set_left_speed(max_speed)
motors.set_right_speed(max_speed)

while True:
    bump_sensors.read()

    if bump_sensors.left_is_pressed():
        motors.set_speeds(0, 0)
        display.fill(0)
        display.text("Left Bump", 0, 0)
        display.show()

        motors.set_left_speed(-max_speed)
        motors.set_right_speed(-max_speed)
        time.sleep_ms(turn_time)
        motors.set_left_speed(max_speed)
        motors.set_right_speed(max_speed)

        display.fill(0)
        display.show()
    
    if bump_sensors.right_is_pressed():
        motors.set_speeds(0, 0)
        display.fill(0)
        display.text("Right Bump", 88, 0)
        display.show()

        motors.set_left_speed(-max_speed)
        motors.set_right_speed(-max_speed)
        time.sleep_ms(turn_time)

        motors.set_left_speed(max_speed)
        motors.set_right_speed(max_speed)

        display.fill(0)
        display.show()