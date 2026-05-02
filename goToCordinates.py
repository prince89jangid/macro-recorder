# ========================= so now test.txt se cordinates lekar mouse move karenga ===============
import pyautogui
import time

mousedelay = 4
keyDelay = 1

pyautogui.PAUSE = 0.5


print("system is ready in 5 seconds")
time.sleep(5)

with open("test.txt", "r") as file:
    content = file.read().strip()
    sub = content.split("\n")

    for r in sub:
        pair = r.split()

        if pair[0].isdigit() == True and pair[1].isdigit() == True:
            x = int(pair[0])
            y = int(pair[1])

            print(x, " ", y)

            pyautogui.click(x, y)
            time.sleep(mousedelay)

        else:

            if pair[0].startswith("'") and pair[0].endswith("'") == True:
                print(pair[0][1])

                print(f"{pair[0][1]}")

                pyautogui.press(f"{pair[0][1]}")
                time.sleep(keyDelay)

            else:
                keyInput = pair[0].split(".")
                pyautogui.press(f"{keyInput[1]}")
                time.sleep(keyDelay)


print("done")
