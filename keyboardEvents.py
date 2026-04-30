from pynput import keyboard


def on_press(key):
    print(f"Pressed: {key}")
    if key == keyboard.Key.esc:
        return False  # listener stop


def on_release(key):
    pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
