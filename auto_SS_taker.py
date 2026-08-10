import pyautogui
import time
import os
import sys

os.makedirs(os.path.join("shots"), exist_ok=True)
print("Auto screenshot taker started. Press Ctrl-C to stop.")

while True:
    # Take the screenshot
    file_name = time.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    pyautogui.screenshot(os.path.join("shots", file_name))
    
    # 10 minutes = 600 seconds
    countdown_seconds = 600 
    
    # Countdown loop
    for remaining in range(countdown_seconds, 0, -1):
        # Calculate minutes and seconds
        mins, secs = divmod(remaining, 60)
        
        # Format the timer string (e.g., 09:59)
        timer = f"{mins:02d}:{secs:02d}"
        
        # Print with \r to overwrite the line, and flush=True to force the terminal to update
        print(f"\rScreenshot taken. Next shot in: {timer}  (Press Ctrl-C to stop)", end="", flush=True)
        time.sleep(1)
        
    # Print a blank line to cleanly separate the next screenshot log
    print()