import time
from pololu_3pi_2040_robot import robot

motors = robot.Motors()

num = input ()
if num == 0:
    motors.set_left_speed(500)
    motors.set_speeds(0,225) # receive 0, power right wheel, turn left
elif num == 1:
    motors.set_right_speed(500)
    motors.set_speeds(225,0) # receive 1, power left wheel, turn right
else:
    print("Invalid input. Please enter 0 or 1.")


