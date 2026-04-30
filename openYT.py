# ============================= this code is detecotr =========================

from pynput import mouse, keyboard


def on_move(x, y):
    pass


def on_click(x, y, button, isPressed):

    if button == mouse.Button.middle:
        return False

    if isPressed == True:
        print(x, " ", y)
        with open("test.txt", "a") as file:
            file.write(f"{x} {y} \n")


def on_press(key):
    if key == keyboard.Key.esc:
        return 
    print(f"you pressed: {key}")


def on_release(key):
    pass


mouseEvent = mouse.Listener(on_move=on_move, on_click=on_click)
keboardEvent = keyboard.Listener(on_press=on_press, on_release=on_release)


# ============================ so that dono ko parallel start kar sake =================

mouseEvent.start()
keboardEvent.start()

mouseEvent.join()
keboardEvent.join()
# ============================== actual logic ===========================

# import pyautogui
# import time

# pyautogui.PAUSE = 0.5


# print('system is ready in 5 seconds')
# time.sleep(5)

# with open("test.txt", "r") as file:
#     content = file.read().strip()
#     sub = content.split("\n")

#     for r in sub:
#         pair = r.split()
#         x = int(pair[0])
#         y = int(pair[1])

#         pyautogui.click(x, y)
#         time.sleep(3)


# print("done")
