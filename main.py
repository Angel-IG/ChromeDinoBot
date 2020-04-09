from PIL import ImageGrab
import numpy as np
import keyboard
import pyautogui
import time

# Constants
# BOX = (?, ?, ?, ?)  # The bot's "vision area"
# JUMP_T = ?  # Each jump is this number of seconds long

print("To use the bot, open Google Chrome, go to chrome://dino, press F11 (fullscreen)"
      " and press SPACE: once you have done that... the computer will play for you!")

print("If the bot is running and you want to terminate the program, press ENTER. \n")

print("Waiting for SPACE... ")
keyboard.wait("space")

print("\nThe bot is playing. Press ENTER to terminate the program...\n")

while True:
    if keyboard.is_pressed("enter"):
        break

    # Bot stuff

print("ENTER pressed. Aborting...")
