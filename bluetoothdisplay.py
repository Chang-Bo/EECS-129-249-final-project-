from machine import Pin, UART
from pololu_3pi_2040_robot import robot
import time

uart = UART(0, 115200, tx=Pin(28), rx=Pin(29), stop = 1, timeout = 10) # Data mode
# uart = UART(0, 38400, bits=8, tx=Pin(28), rx=Pin(29), stop = 1, timeout = 10) # Command mode
led = Pin(25, Pin.OUT)

display = robot.Display()

while True:
  data = uart.read()
  time.sleep(2)
  led.value(0)  # yellow LED on
  time.sleep(2)
  led.value(1)  # yellow LED off
  display.fill(0)
  display.text(str(data)+ " " + "EECS", 0, 0)
  display.show()