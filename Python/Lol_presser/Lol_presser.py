# Required packages:
# python -m pip install pyautogui
# python -m pip install pillow
# python -m pip install pyscreeze
# python -m pip install opencv-python
# python -m pip install keyboard
#
# Or install everything at once:
# python -m pip install pyautogui pillow pyscreeze opencv-python keyboard

import pyautogui
import time
from random import uniform
from keyboard import is_pressed

while True:

    if is_pressed("q"): # Hold the key down
        print("Stopping...")
        break

    try:
        location = pyautogui.locateOnScreen("Accept.png",confidence=0.8)
        time.sleep(uniform(1,3))
        pyautogui.click(location)
        # Prevent repeated clicks on the same accept button
        time.sleep(5)

    except pyautogui.ImageNotFoundException:
        time.sleep(1)  # wait 1 second before checking again