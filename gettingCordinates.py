# ============================= this code is detect cordinates and save in test.txt =========================

from pynput import mouse, keyboard


def on_click(x, y, button, isPressed):

    if button == mouse.Button.middle:
        return False

    if isPressed == True:
        print(x, " ", y)
        with open("test.txt", "a") as file:
            file.write(f"{x} {y} \n")


def on_press(key):
    if key == keyboard.Key.esc:
        print("esc pressed")
        return False
    
    
    print(f"{key}")
    
    
    with open("test.txt", "a") as file:
        file.write(f"{key} \n")


def on_release(key):
    pass


def on_move(x, y):
    pass


mouseEvent = mouse.Listener(on_move=on_move, on_click=on_click)
keboardEvent = keyboard.Listener(on_press=on_press, on_release=on_release)


mouseEvent.start()
keboardEvent.start()

mouseEvent.join()
keboardEvent.join()
