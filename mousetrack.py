
#===============================  FOR GETTING CURSOR INFORMATION =====================================

from pynput import mouse


def handle_mouse_movement(x, y):
    print(f"[MOVE] Position: {x}, {y}")


def handle_mouse_click_event(x, y, btn, is_pressed):
    if is_pressed:
        print(f"[CLICK] Position: {x}, {y}")


# Listener setup
with mouse.Listener(
    on_move=handle_mouse_movement,
    on_click=handle_mouse_click_event,
) as my_listener:

    my_listener.join()











