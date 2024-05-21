import gpiozero
import time

Relay_Ch1 = 26

# Triggered by ouput pin being switched ON: active_high=True
# Initially open (NO) contact: initial_value=False

relay1 = gpiozero.OutputDevice(Relay_Ch1, active_high=True, initial_value=False)

print("Setup The Relay Module is [success]")

try:
        while True:
                #Control the Channel 1
                relay1.on()    # the actuactor will extract/wait
                print(relay1.value)
                print("Channel 1:The Common Contact is access to the Normal Open Contact!")
                time.sleep(60*3) # Wait for 3 minutes
                relay1.off()   # the actuactor will extend out
                print(relay1.value)
                print("Channel 1:The Common Contact is access to the Normal Closed Contact!\n")
                time.sleep(60*60) # Wait for 1 hour

except:
        print("except")
        #GPIO.cleanup()
