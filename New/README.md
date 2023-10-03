# E7 Secret Shop Auto Refresh Macro

This macro helps the user refresh the Secret Shop and buy Covenant and Mystic bookmarks. The mouse clicks and delay intervals are randomized to avoid Epic Seven detecting the use of third-party software. 

![](https://media.giphy.com/media/NSAX9N2SyPUVrih2E0/giphy-downsized-large.gif)

## How to Run:
1. Get the lastest update of [Python](https://www.python.org/downloads/)
	> After installing each python verion, click on them again then modify, after that you should click all of the optional upgrades and settings that you can click
	> Then open command prompt, and install the dependencies listed below
2. This Script currently only work on android subsystem for windows 11, I don't have windows 10 so I don't know if it will works on other emulator, but on bluestack it doesn't work as the emulator isn't compatible with virtual click from OS 
3. You can set the custom resolution after inputting for how long the code will run (for example 2k monitor is 2560x1440 (width x height))
4. Open Epic Seven, Maximize the game window, then enter Secret Shop
5. Run the Python script
	>If running from terminal, make sure the refresh button is visible on the screen
6. If running the script for the first time, make sure everything works correctly first
	>If the macro is not recognizing the images properly, you will need to replace the images in the folder with your own screenshots
7. To exit the script, you have to press Ctrl + C in the terminal
    > Script will exit right away.

## Dependencies to Install
Use the package manager [pip](https://pip.pypa.io/en/stable/installation/) to install the following dependencies:
Or when you install python on Windows, you will have to click all the optional so that you can you pip in cmd prompt
```
pip install keyboard
pip install opencv-python
pip install pyautogui
pip install pillow
```
