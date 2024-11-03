# import win32api, win32con, win32ui, win32gui
import pyautogui as pg
from pynput.keyboard import Key, Controller as KeyController
from pynput.mouse import Button, Controller as ButtonController
import numpy as np
import keyboard as kb
from windowsCapture import WindowsCaptureClass
import cv2 as cv

wincap = WindowsCaptureClass("Roblox")

state = 0

while True:
    screenshot = wincap.sscreenshot()
    if state == 0:
        try:
            all = pg.locate('alltab.png', screenshot, confidence=0.65, grayscale=True)
            # pg.moveTo(all)
            state = 1
        except pg.ImageNotFoundException:
            print("not found")

    if state == 1:
        wpos = 0
        fpos = 0
        try:
            wpos = pg.locate('intab.png', screenshot, confidence=0.45, grayscale=True, region=all).left
            # pg.moveTo(wpos)
            state = 1
        except pg.ImageNotFoundException:
            pass

        try:
            fpos = pg.locate('fishtab.png', screenshot, confidence=0.45, grayscale=False, region=all).left
            # pg.moveTo(fpos)
        except pg.ImageNotFoundException:
            # pg.moveTo(wpos)
            pass
    
        error = fpos - wpos
        if error>0:
            print("move >>", fpos, wpos)
        elif error == 0 or fpos == 0 or wpos == 0:
            print("move ||")
        else:
            print("move <<", fpos, wpos)
            


    if kb.is_pressed('q'):
        cv.destroyAllWindows()
        break