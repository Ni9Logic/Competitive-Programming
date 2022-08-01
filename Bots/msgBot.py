import pyautogui as pg

import time

time.sleep(5)

text = open('animals.txt', 'r')
msg = "Ai_sha is a "
for i in text:
    print(msg + i)
    pg.write(msg + i)
    pg.press('Enter')
    