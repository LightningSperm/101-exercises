from pynput.keyboard import Key, Controller, Listener
import pyautogui


ctrl = Controller()

st = 1
ft = 0.008

def forward_or_backward():
    pass

def hadoken(direction):
    pyautogui.keyDown('down')
    pyautogui.keyDown(direction)
    pyautogui.keyUp('down')
    pyautogui.keyDown('q')
    pyautogui.keyUp(direction)
    pyautogui.keyUp('q')
    print("shinku hadsoken!")

def tatsunaki(direction):
    pyautogui.keyDown('down')
    pyautogui.keyDown(direction)
    pyautogui.keyUp('down')
    pyautogui.keyDown('e')
    pyautogui.keyUp(direction)
    pyautogui.keyUp('e')

def shinku_hadoken(direction):
    pyautogui.keyDown('down')
    pyautogui.keyDown(direction)
    pyautogui.keyUp('down')
    pyautogui.keyUp(direction)
    pyautogui.keyDown('down')
    pyautogui.keyDown(direction)
    pyautogui.keyUp('down')
    pyautogui.keyDown('q')
    pyautogui.keyUp(direction)
    pyautogui.keyUp('q')

def shoryuken(direction):

    pyautogui.keyDown(direction)
    pyautogui.keyUp(direction)
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')
    pyautogui.keyDown('q')
    pyautogui.keyDown(direction)
    # pyautogui.keyDown('up')
    pyautogui.keyUp(direction)
    pyautogui.keyUp('q')

def on_press(key):
    try:
        print(f'alphanumeric key {key.char} pressed')
        if key.char == '1':
            print("Hadoken!")
            shoryuken('right')
        elif key.char == '3':
            print("Taaaatsunaki")
            tatsunaki('left')
        elif key.char == '5':
            print("SHINKUUUUUUU_HADOKEN!")
            shinku_hadoken('right')
        elif key.char == '2':
            print("Hadoken!")
            hadoken('left')
        elif key.char == '4':
            print("Taaaatsunaki")
            tatsunaki('right')
        elif key.char == '6':
            print("SHINKUUUUUUU_HADOKEN!")
            shinku_hadoken('left')
    except AttributeError:
        print('special key {key} pressed')
 

def on_release(key):
    print('{0} released'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    
        
listener = Listener(
    on_press=on_press,
    on_release=on_release)


listener.start()