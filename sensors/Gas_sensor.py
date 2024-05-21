import time, sys
import os
from gpiozero import DigitalInputDevice, MCP3008

# Set up GPIO pin 13 for reading gas
gasPin = DigitalInputDevice(13)

try:
    while True:
        # Determine if gas is present (i.e., LOW signal)
        if (gasPin.value == 0):
            gas_state = "No gas leaks"
        else:
            gas_state = "WARNING: Gas is detected!!"
            with open('object_ident_4.py', 'r') as file:
                code = file.read()
                exec(code)

        # Print the gas state
        print(f"Gas State: {gas_state}")

        time.sleep(1)  # Wait for a short period before reading again

except KeyboardInterrupt:
    print("Gas detection stopped by user")
    exit()
