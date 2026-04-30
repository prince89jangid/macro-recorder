# ============================= this code is detect cordinates and save in test.txt =========================

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


with mouse.Listener(on_move=on_move, on_click=on_click) as listner:
    listner.join()


print('ho gaye na get') 