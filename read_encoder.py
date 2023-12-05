import time
from machine import Pin
from pololu_3pi_2040_robot import robot
from machine import Pin, UART

display = robot.Display()
motors = robot.Motors()
encoders = robot.Encoders()

while True:
    uart = UART(0, 115200, tx=Pin(28), rx=Pin(29), stop = 1, timeout = 10) 

    display.fill_rect(40, 48, 64, 16, 0)
    left_encoder, right_encoder = encoders.get_counts()
    display.text(f"{left_encoder:>8}", 30, 48)
    display.text(f"{right_encoder:>8}", 40, 56)
    
    display.show()