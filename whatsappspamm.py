import webbrowser

import pyautogui
import webbrowser
import time


webbrowser.open_new("https://web.whatsapp.com/")
time.sleep(30)
for i in range(10):
    pyautogui.press("h")
    pyautogui.press("i")
    pyautogui.press("enter")
