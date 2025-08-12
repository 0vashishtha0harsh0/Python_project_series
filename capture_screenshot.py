import os
import time
import pyautogui
from datetime import datetime

folder_name = "Screenshot_by_automation"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

interval = int(input("Enter the number of Intervals : "))

total_screenshots = interval

print("Starting capturing screenshot after every {interval} seconds......")

for i in range(total_screenshots):
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    file_name = os.path.join(folder_name,f"Screenshot_{timestamp}.png")
    screenshot = pyautogui.screenshot()

    screenshot.save(file_name)
    print(f"[{i+1}] Screenshot saved : {file_name}")
    time.sleep(interval)

print("screenshot capturing completed")
               
