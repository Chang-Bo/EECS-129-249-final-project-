import time
from machine import Pin
from pololu_3pi_2040_robot import robot
from machine import Pin, UART


uart = UART(0, 115200, tx=Pin(28), rx=Pin(29), stop = 1, timeout = 10) # Data mode
# uart = UART(0, 38400, bits=8, tx=Pin(28), rx=Pin(29), stop = 1, timeout = 10) # Command mode
#led = Pin(25, Pin.OUT)

display = robot.Display()
motors = robot.Motors()
while True:
  data = uart.read()
  time.sleep(2)
  #led.value(0)  # yellow LED on
  #time.sleep(2)
  #led.value(1)  # yellow LED off
  display.fill(0)
  display.text(str(data), 0, 0)
  display.show()

  if data == b'0':
    time.sleep(2)
    display.fill(0)
    display.text("   "+"yes", 0, 0)
    display.show()
    motors.set_left_speed(500)
    motors.set_right_speed(500)
  else:
    uart.write(b'Hello')
    '''motors.set_speeds(0,225) # receive 0, power right wheel, turn left
    elif data == 1:
    time.sleep(2)
    display.fill(0)
    display.text("no", 0, 0)
    display.show()
    motors.set_speeds(225,0) # receive 1, power left wheel, turn right'''