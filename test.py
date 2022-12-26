import win32api,win32con

if __name__ == "__main__":
    print(win32api.GetCursorPos())
    win32api.SetCursorPos((200,155))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
    print(win32api.GetCursorPos())