import win32api, win32con, win32gui, win32ui
import numpy as np

class WindowsCaptureClass:
    w = 0 # set this
    h = 0 # set this
    hwnd = 0
    # cropped_x = 0
    # cropped_y = 0

    def __init__(self, window_name=None) -> None:
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            # set to capture that screen
            self.hwnd = win32gui.FindWindow(None, "Roblox")
            if not self.hwnd:
                raise Exception('Window not Found: {}'.format(window_name))

        # window_rect = win32gui.GetWindowRect(self.hwnd)
        # self.w = window_rect[2] - window_rect[0]
        # self.h = window_rect[3] - window_rect[1]
        self.w = 1920
        self.h = 1080

        # border_pixels = 8
        # titlebar_pixels = 30
        # self.w = self.w - (border_pixels * 2)
        # self.h = self.h - titlebar_pixels - border_pixels
        # self.cropped_x = border_pixels
        # self.cropped_y = titlebar_pixels


    def sscreenshot(self):
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (0, 0), win32con.SRCCOPY)

        signIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        # save the screenshot (fps)
        # dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)

        img = img[...,:3]

        img = np.ascontiguousarray(img)

        return img
    
    @staticmethod
    def list_window_names():
        def winEnumHandler (hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print("hex :", hex(hwnd), "| name :", win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)

    # list_window_names()