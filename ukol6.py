import random
import hashlib
from pynput import mouse, keyboard # type: ignore
from datetime import datetime

# Sběr z pohybu myši
mouse_data = []

def on_move(x, y):
    timestamp = datetime.now().timestamp()
    mouse_data.append((x, y, timestamp))

def on_click(x, y, button, pressed):
    if pressed:
        timestamp = datetime.now().timestamp()
        mouse_data.append((x, y, timestamp))

def on_scroll(x, y, dx, dy):
    timestamp = datetime.now().timestamp()
    mouse_data.append((dx, dy, timestamp))

# Sběr z úhozů na klávesnici
keyboard_data = []

def on_press(key):
    try:
        timestamp = datetime.now().timestamp()
        keyboard_data.append((key.char, timestamp))
    except AttributeError:
        timestamp = datetime.now().timestamp()
        keyboard_data.append((str(key), timestamp))

# Start sběru dat
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
keyboard_listener = keyboard.Listener(on_press=on_press)

mouse_listener.start()
keyboard_listener.start()

# Zastavení sběru dat po určité době (např. 10 sekund)
import time
time.sleep(10)

mouse_listener.stop()
keyboard_listener.stop()

# Kombinování nasbíraných dat a vytvoření seed
combined_data = mouse_data + keyboard_data
combined_string = ''.join(map(str, combined_data))
seed = int(hashlib.sha256(combined_string.encode()).hexdigest(), 16) % (10**8)

print(f"Vygenerovaný seed: {seed}")
