import pyautogui, time, PIL

def press_spc():
    print('jump')
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')

def count_black():
    blck = 0 
    captured = pyautogui.screenshot(region=(245, 300, 30, 90)) #play around with the position
    for i in range(30):
        for j in range(90):
            r, g, b = captured.getpixel((i, j))
            if (r + g + b != (3 * 255)):
                blck += 1    
    return blck

while True:
    bl = count_black()
    if bl > 60:
        press_spc()
    
