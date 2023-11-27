# Directory Path containing csv file
DIRECTORY_PATH = r'C:\Users\spart\Desktop\Python\WhatsApp'

# Configurable parameters for send_whatsapp_messages function
CONTINUE_TO_CHAT_BUTTON_LOC = (953, 424)     # Get the coordinates by using mouse_coordinates.py
DIST_CONTINUE_CHAT_TO_USE_WHATSAPP_WEB = 79  # Adjust the value according to your screensize
INITIAL_WAIT_DURATION = 3                    # Change the time depeding on your system speed
WHATSAPP_LOADING_DURATION = 10               # Change the duration based on your chrome loading capacity
FINAL_WAIT_DURATION = 2                      # Change the time depending on your system speed

# Change the text depending on the training program needs
WHATSAPP_TEXT = """This is a reminder message from Spartificial. 
The training program that you have enrolled for is starting today at 7:00 PM. 
To get the joining link of the session please join our Slack workspace if you haven't already.
The Slack invitation was sent to your registered email ID. 

Reach out to me in case of any difficulties joining the Slack workspace! 

Thanks, we shall see you in the session at 7:00 PM!"""