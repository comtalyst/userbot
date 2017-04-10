
from pykeyboard import PyKeyboard
import time

k = PyKeyboard()
k.press_key(k.alt_key)          # alt-tab to text editor
k.press_key(k.tab_key)
k.release_key(k.alt_key)
k.release_key(k.tab_key)
time.sleep(0.1)                 # delay 0.1 seconds
k.type_string("Hello World!")   # type "Hello World!"

