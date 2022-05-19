import pyautogui as pg

import time

time.sleep(5)

text = open('Bots/fish.txt', 'r')
hamza = "Fazal is a "



for i in text:
    pg.write(hamza + i)
    pg.press('Enter')
    