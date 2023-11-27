import utility
import pandas as pd
import config

# Configurable parameters for send_whatsapp_messages function
directory_path = config.DIRECTORY_PATH
continue_to_chat_button_loc = config.CONTINUE_TO_CHAT_BUTTON_LOC
dist_continue_chat_to_use_whatsapp_web = config.DIST_CONTINUE_CHAT_TO_USE_WHATSAPP_WEB
initial_wait_duration = config.INITIAL_WAIT_DURATION
whatsapp_loading_duration = config.WHATSAPP_LOADING_DURATION
final_wait_duration = config.FINAL_WAIT_DURATION
whatsapp_text = config.WHATSAPP_TEXT

# Define file names and column titles
TARGET_FILE_NAME = 'data.csv'
CSV_FILE_EXTENSION = '.csv'
NAME_COLUMN_KEYWORDS = ['name']
NUMBER_COLUMN_KEYWORDS = ['phone', 'number']

def main():
    """
    Simulate The Process of Sending Bulk Messages on WhatsApp
    - This is used to send a reminder message to students of Spartificial on WhatsApp
    - It needs one csv file that has name and number information
    - Students must have Indian phone numbers
    """
    
    # Generate dataframe from csv file
    df = utility.csv_to_dataframe(directory_path=directory_path, 
                                  target_file_name=TARGET_FILE_NAME, 
                                  file_extension=CSV_FILE_EXTENSION)
    
    # Extracting the column titles from the datadrame for name and phone number
    names_numbers_col_title = utility.extract_column_titles(dataframe=df, 
                                                            name_keywords=NAME_COLUMN_KEYWORDS, 
                                                            number_keywords=NUMBER_COLUMN_KEYWORDS)
    
    # Generating lists for names and respective phone numbers
    names, numbers = utility.extract_names_numbers(dataframe=df, 
                                                   name_column=names_numbers_col_title[0], 
                                                   number_column=names_numbers_col_title[1])
    
    # Encoding whatsapp_text in whatsapp url format 
    text = utility.url_encode_text(whatsapp_text)

    # Send the messages to names on their respective numbers using pyautogui
    utility.send_whatsapp_messages(numbers, 
                                   names, 
                                   message_text=text,
                                   continue_to_chat_button_loc=continue_to_chat_button_loc,
                                   dist_continue_chat_to_use_whatsapp_web=dist_continue_chat_to_use_whatsapp_web,
                                   initial_wait_duration=initial_wait_duration,
                                   whatsapp_loading_duration=whatsapp_loading_duration,
                                   final_wait_duration=final_wait_duration)


if __name__ == "__main__":
    main()