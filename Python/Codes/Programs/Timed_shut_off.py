import pyautogui
import time

# 1 hora = 3600
# 30 min = 1800
sec = 1800

pyautogui.FAILSAFE = False
time.sleep(sec)
pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.click(x=20, y=705)
pyautogui.click(x=37, y=633)
pyautogui.click(x=37, y=633)