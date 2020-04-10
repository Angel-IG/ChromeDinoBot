from PIL import ImageGrab
import numpy as np
import keyboard
import pyautogui
import time

# Constants
BOX = (261, 519, 563, 627)  # The bot's "vision area"
JUMP_T = 0.5  # Each jump is this number of seconds long

pyautogui.FAILSAFE = False


def obstacle(area):
    # If all the pixels are equal, there isn't any
    # obstacle, but otherwise the bot has to jump.

    val = area[0, 0]
    for i in area:
        for j in i:
            if j != val:
                return True

    return False


def main():
    print("To use the bot, open Google Chrome, go to chrome://dino, press F11 (fullscreen)"
          " and press SPACE: once you have done that... the computer will play for you!")

    print("If the bot is running and you want to terminate the program, press ENTER. \n")

    print("Waiting for SPACE... ")
    keyboard.wait("space")

    print("\nThe bot is playing. Press ENTER to terminate the program...\n")

    while True:
        if keyboard.is_pressed("enter"):
            break

        screen = np.array(ImageGrab.grab(bbox=BOX))[:, :, 0]

        if obstacle(screen):
            # Jump
            pyautogui.keyDown("space")
            time.sleep(JUMP_T)
            pyautogui.keyUp("space")

    print("ENTER pressed. Aborting...")


main()
