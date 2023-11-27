'''
Run this code to get your mouse coordinates on your screen.
- This code allows you to set your mouse for 5 seconds before displaying the output
- Use this output as x and y values for the whatsapp.py file

Follow these steps to get proper mouse coordinates:
1. Run this code and it shall redirect you to chrome
2. Hover your mouse on "Continue to Chat" within 5 seconds
3. Don't move your mouse until 5 seconds
4. Come back and check the output of x and y
5. Copy and Paste it to whatsapp.py where "Continue to Chat coordinates are being used
6. Rerun this code and click on "Continue to Chat"
7. Within 5 seconds hover your mouse on "Use WhatsApp Web"
8. Come back and check the output of x and y and use it in whatsapp.py to click this button 
'''

import pyautogui
import time 
import os
link = 'https://wa.me/911234567890?text=Hey%2C%20%0A%0AThis%20is%20Demo%20Text.%0A%0AThanks%21'
os.system(f"start chrome {link}")
print("Please position the cursor over the button to get the mouse coordinates.")
time.sleep(5)
button_pos = pyautogui.position()
print(f"Button coordinates: {button_pos}")
