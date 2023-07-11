# E7 Secret Shop Auto Refresh Macro

This macro helps the user refresh the Secret Shop and buy Covenant and Mystic bookmarks. The mouse clicks and delay intervals are randomized to avoid Epic Seven detecting the use of third-party software. 

This code is a modification from the original by [dengpris](https://github.com/dengpris/E7-Secret-Shop-Auto-Refresher)

![](https://media.giphy.com/media/NSAX9N2SyPUVrih2E0/giphy-downsized-large.gif)

## How to Run:
1. Make sure you have [Python version 3.10](https://www.python.org/downloads/release/python-31011/) and also [Python version 3.11](https://www.python.org/downloads/release/python-3114/)  and the correct dependencies installed (see below)
	> After installing each python verion, click on them again then modify, after that you should click all of the optional upgrades and settings that you can click on for both versions
	> Then open command prompt, and install the dependencies listed below
2. Set your resolution to 1920x1080. This macro will not work for other resolutions. Otherwise you will have to replace all the png files with your own
3. Open and maximize Bluestacks, E7 on Window 11, any Emulator would do
4. Open Epic Seven, then enter Secret Shop
5. Run the Python script
	>If running from terminal, make sure the refresh button is visible on the screen
6. If running the script for the first time, make sure everything works correctly first
	>If the macro is not recognizing the images properly, you will need to replace the images in the folder with your own screenshots
7. To exit the script, hold 'q' until the macro stops working completely
    > Script will exit after confirming refresh. Set 'debug_timer' greater than 0 to exit before refresh.

## Dependencies to Install
Use the package manager [pip](https://pip.pypa.io/en/stable/installation/) to install the following dependencies:
Or when you install python on Windows, you will have to click all the optional so that you can you pip in cmd prompt
```
pip install keyboard
pip install opencv-python
pip install pyautogui
pip install mouse
pip install pillow
pip install pywin32
```
