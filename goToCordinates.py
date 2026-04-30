# ========================= so now test.txt se cordinates lekar mouse move karenga ===============
import pyautogui
import time

openingTime = 1

pyautogui.PAUSE = 0.5


print("system is ready in 5 seconds")
# time.sleep(5)

with open("test.txt", "r") as file:
    content = file.read().strip()
    sub = content.split("\n")

    for r in sub:
        pair = r.split()

        if pair[0].isdigit() == True and pair[1].isdigit() == True:
            x = int(pair[0])
            y = int(pair[1])

            pyautogui.click(x, y)

        else:

            if pair[0].startswith("'") and pair[0].endswith("'") == True:
                print(pair[0][1])
                
                pyautogui.press(f"{pair[0][1]}")

        time.sleep(openingTime)


print("done")
