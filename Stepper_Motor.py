import time, sys
from gpiozero import OutputDevice

direction_pin = OutputDevice(20)
step_pin = OutputDevice(21)

try:
#    while True:
    print('Direction clockwise')
    time.sleep(1)
    direction_pin.on()
    for x in range(200):
        step_pin.on()
        time.sleep(0.05)
        step_pin.off()
        time.sleep(0.05)

    print('Direction anti-clockwise')
    time.sleep(3)
    direction_pin.off()
    for x in range(200):
        step_pin.on()
        time.sleep(0.05)
        step_pin.off()
        time.sleep(0.05)

except KeyboardInterrupt:
    exit()
