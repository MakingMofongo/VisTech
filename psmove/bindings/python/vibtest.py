import psmoveapi
import time
# Connect to the first connected controller
move = psmoveapi.PSMoveAPI()

# Set the vibration intensity (0-255)
move.set_rumble(255)

# Apply the vibration for a certain duration (in seconds)
move.update_leds()
time.sleep(0.5)

# Turn off the vibration
move.set_rumble(0)
move.update_leds()