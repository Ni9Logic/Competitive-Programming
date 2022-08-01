import pyautogui as pg

import time

time.sleep(5)

text = open('love.txt', 'r')
for i in text:
    print(i)
    pg.write(i)
    pg.press('Enter')
    