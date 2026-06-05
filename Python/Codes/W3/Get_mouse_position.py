import pyautogui
import time

pyautogui.PAUSE = 1

time.sleep(3)

Screen = pyautogui.position()

x, y = Screen

print(f'pyautogui.click(x={x}, y={y})')