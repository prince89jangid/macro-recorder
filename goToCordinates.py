# ========================= so now test.txt se cordinates lekar mouse move karenga ===============
import pyautogui
import time

openingTime = 1

pyautogui.PAUSE = 0.5


print("system is ready in 5 seconds")
time.sleep(5)

with open("test.txt", "r") as file:
    content = file.read().strip()
    sub = content.split("\n")

    for r in sub:
        pair = r.split()
        x = int(pair[0])
        y = int(pair[1])

        pyautogui.click(x, y)
        time.sleep(openingTime)


print("done")
