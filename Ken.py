from pynput.keyboard import Key, Controller, Listener
import pyautogui



 
# def show(key):
 
#     print('\nYou Entered {0}'.format( key))
 
#     if key == Key.delete:
#         # Stop listener
#         return False0987
 
# # Collect all event until released
# with Listener(on_press = show) as listener:   
#     listener.join()


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
    # pyautogui.hotkey('down','right',interval=ft)
    # pyautogui.hotkey('down','right',interval=ft)
    # pyautogui.hotkey('s',interval=st)
    # pyautogui.hotkey('right','s',interval=timing)
    # pyautogui.hotkey('s')
               # pyautogui.hotkey('down','right',interval=timing)
    # pyautogui.hotkey('right')
    # pyautogui.hotkey('s')
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

    # pyautogui.press([direction, 'down', direction, 'q'],interval=st)
    # pyautogui.press('down',interval=ft)
    # # pyautogui.press(direction,interval=ft)
    # pyautogui.hotkey(direction, 'q')
    # pyautogui.keyDown(direction)
    # pyautogui.keyUp(direction)
    # pyautogui.keyDown('down')
    # pyautogui.keyUp('down')
    # pyautogui.hotkey(direction, 'q')
    # pyautogui.keyUp(direction)
    # pyautogui.keyDown('down')
    # pyautogui.keyUp('down')
    # pyautogui.keyDown('q')
    # pyautogui.keyUp(direction)
    # pyautogui.keyUp('q')

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