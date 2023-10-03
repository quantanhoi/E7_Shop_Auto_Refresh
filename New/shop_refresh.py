import pyautogui
import time
import random
import keyboard


# Set the duration in minutes
duration_minutes = float(input("Script will run for (enter in minute): "))



# Convert the duration to seconds
duration_seconds = duration_minutes * 60

# Get the start time
start_time = time.time()

mystic_bought = 0
covenant_bought = 0

buy_button_pos_x = 800
buy_button_pos_y = 40
default_confidence = 0.8

def delay_visual():
    delay_visual = random.uniform(2, 2.5)
    return delay_visual

def delay_interval():
    delay_interval = random.uniform(0.2, 0.5)
    return delay_interval

def rand_drag_y():
    drag_range = random.randrange(-600, -400)
    return drag_range

def rand_drag_x():
    drag_range = random.randrange(-50, 50)
    return drag_range

def mouse_click_rb(RB_pos):
    x, y = pyautogui.center(RB_pos)
    rand_x = random.randrange(-60, 60)
    rand_y = random.randrange(-15, 15)
    x += rand_x
    y += rand_y
    # Click at the center coordinates
    pyautogui.click(x, y, clicks=2, interval=delay_interval())

def mouse_click_buy(BM_pos):
    x, y = pyautogui.center(BM_pos)
    rand_x = random.randrange(-60, 60)
    rand_y = random.randrange(-15, 15)
    x += buy_button_pos_x + rand_x
    y += buy_button_pos_y + rand_y
    # Click at the center coordinates
    pyautogui.click(x, y, clicks=2, interval=delay_interval())
    

def scroll():
    width, height = pyautogui.size()

    # Calculate the coordinates for the middle of the right side of the screen
    x = width * (3/4)
    y = height // 1.2
    rand_x = random.randrange(-60, 60)
    rand_y = random.randrange(-15, 15)
    x += rand_x
    y += rand_y
    # Move the mouse cursor to the calculated coordinates
    pyautogui.moveTo(x, y)

    # Scroll down
    pyautogui.mouseDown()
    pyautogui.dragRel(rand_drag_x(), rand_drag_y(), duration=delay_interval())
    pyautogui.mouseUp()

def confirm_refresh():
    confirm_refresh_pos = pyautogui.locateOnScreen("confirm_refresh.png", confidence= default_confidence)
    if(confirm_refresh_pos is not None):
        mouse_click_rb(confirm_refresh_pos)
    
def refresh():
    RB_pos = pyautogui.locateOnScreen('refresh_button.png', confidence=default_confidence)
    # Check if the image was found
    if RB_pos is not None:
        mouse_click_rb(RB_pos)
        time.sleep(delay_interval())
        confirm_refresh()
        
    else:
        print("refresh button not found")
        


def confirm_buy(BM_type):
    global covenant_bought
    global mystic_bought
    if(BM_type == "Covenant"):
        confirm_pos = pyautogui.locateOnScreen("covenant_confirm.png", confidence=default_confidence)
        if(confirm_pos is None):
            return False
        
        #using mouse click for refresh button here
        mouse_click_rb(confirm_pos)
        print("confirm buy covenant")
        covenant_bought += 5
        
    if(BM_type == "Mystic"):
        confirm_pos = pyautogui.locateOnScreen("mystic_confirm.png", confidence=default_confidence)
        if(confirm_pos is None):
            return False
        #using mouse click for refresh button here
        mouse_click_rb(confirm_pos)
        print("confirm buy mystic")
        mystic_bought += 50
    return True

def find_covenant():
    BM_pos = pyautogui.locateOnScreen('covenant.png', confidence=default_confidence)
    if BM_pos is not None:
        mouse_click_buy(BM_pos)
        time.sleep(delay_visual())
        confirm_buy("Covenant")
        return True
    else:
        return False

def find_mystic():
    BM_pos = pyautogui.locateOnScreen('mystic.png', confidence=default_confidence)
    if BM_pos is not None:
        mouse_click_buy(BM_pos)
        time.sleep(delay_visual())
        confirm_buy("Mystic")
        return True
    else:
        return False


def refresh_loop():
    time.sleep(delay_visual())
    refresh()
    time.sleep(delay_visual())

def print_bought():
    print("Covenant count: " + str(covenant_bought))
    print("Mystic count: " + str(mystic_bought))
    
def loop():
    while True:
        try:
            find_covenant()
            find_mystic()
            scroll()
            time.sleep(delay_interval())
            find_covenant()
            find_mystic()
            refresh_loop()
            elapsed_time = time.time() - start_time
            if elapsed_time >= duration_seconds:
                break
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    loop()
    print_bought()

