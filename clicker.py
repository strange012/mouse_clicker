import random

import win32api, win32con
import time
import math

import pyautogui
def main_win32():
    DELAY_MAX = 0.01
    DELAY_MIN = 0.00001
    DELAY_STEP = 0.0005

    SIZE = 1000

    delay = 0.0015

    mode_count = 5
    mode = 0

    state_up_key = win32api.GetKeyState(0x26)
    state_down_key = win32api.GetKeyState(0x28) 
    state_left_key = win32api.GetKeyState(0x25)
    state_right_key = win32api.GetKeyState(0x27) 

    i = 0

    while True:
        up =  win32api.GetKeyState(0x26)
        down = win32api.GetKeyState(0x28) 
        left = win32api.GetKeyState(0x25)
        right = win32api.GetKeyState(0x27)

        if mode == 0:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, random.randint(-20, 20), random.randint(-20, 20))
        elif mode == 1:
            x = int(960 + math.sin(math.pi*2*i/1000)*960)
            y = int(540 + math.cos(math.pi*4*i/1000)*540)
            win32api.SetCursorPos((x,y))
        elif mode == 2:
            x = int(960 + math.sin(math.pi*4*i/1000)*960)
            y = int(540 + math.cos(math.pi*2*i/1000)*540)
            win32api.SetCursorPos((x,y))
        elif mode == 3:
            x = int(960 + math.sin(math.pi*8*i/1000)*960)
            y = int(540 + math.cos(math.pi*i/1000)*540)
            win32api.SetCursorPos((x,y))
        elif mode == 4:
            x = int(960 + math.cos(math.pi*i/1000)*960)
            y = int(540 + math.sin(math.pi*8*i/1000)*540)
            win32api.SetCursorPos((x,y))
        else:
            pass

        if win32api.GetKeyState(0x01) < 0: 
            break
        
        if up != state_up_key:  # UP ARROW key state changed
            state_up_key = up
            if up < 0:
                delay = min(DELAY_MAX, delay + DELAY_STEP)
                print(delay)
                
        if down != state_down_key:  # DOWN ARROW Key state changed
            state_down_key = down
            if down < 0:
                delay = max(DELAY_MIN, delay - DELAY_STEP)
                print(delay)

        if left != state_left_key:  # DOWN ARROW Key state changed
            state_left_key = left
            if left < 0:
                mode = (mode - 1) % mode_count
                print(mode)

        if right != state_right_key:  # DOWN ARROW Key state changed
            state_right_key = right
            if right < 0:
                mode = (mode + 1) % mode_count
                print(mode)

        i = (i + 1) % SIZE
        time.sleep(delay)

if __name__ == '__main__':
    main_win32()