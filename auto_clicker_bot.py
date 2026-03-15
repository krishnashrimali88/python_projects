import time
import threading
from pynput.mouse import Controller,Button
from pynput.keyboard import Listener,KeyCode

STOP_KEY = KeyCode(char="t")

mouse = Controller()
running = True


def clicker():
    while running:
        mouse.click(Button.left,1)
        time.sleep(0.1)
        
       
def on_press(key):
    if key == STOP_KEY:
        global running
        running = False
        return False


click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=on_press) as listener:
    listener.join()



