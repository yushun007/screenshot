import os
import ctypes
import multiprocessing
import win32gui,win32con,win32api
import time
from PIL import ImageGrab


def screenshot(top_x,top_y,down_x,down_y):
    im = ImageGrab.grab((top_x,top_y,down_x,down_y))
    im.save(r'E:\python\test.png')

def find_window(name):
    handle = win32gui.FindWindow(0,name)
    window_attr = []
    window_attr.append(win32gui.GetClassName(handle))
    window_attr.append(win32gui.GetWindowText(handle))
    window_attr.append(win32gui.GetWindowRect(handle))
    print(window_attr[2][1])
    print(window_attr[2][2])
    screenshot(window_attr[2][0],window_attr[2][1],window_attr[2][2],window_attr[2][3])
    win32api.SetCursorPos((window_attr[2][2]-20,window_attr[2][1]+20))
#    ctypes.windll.user32.SetCursorPos(window_attr[2][2]-3,window_attr[2][1]+3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)


if __name__ == "__main__":
    p = multiprocessing.Process(target=os.system,args=('compmgmt.msc',))
    p.start()
    time.sleep(2)
    name = "计算机管理"
    find_window(name)