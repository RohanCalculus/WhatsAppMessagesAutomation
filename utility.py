import os
import time
import pyautogui
import urllib.parse
import pandas as pd

def csv_to_dataframe(directory_path, target_file_name, file_extension):
    """
    Rename CSV files in the specified directory to the target file name.

    Parameters:
    - directory_path (str): The path to the directory containing CSV files.
    - target_file_name (str): The desired target file name (default is 'data.csv').
    
    Returns:
    - str: The path of the renamed CSV file.
    """
    files = os.listdir(directory_path)

    for file_name in files:
        if file_name.endswith(file_extension):
            old_path = os.path.join(directory_path, file_name)
            new_path = os.path.join(directory_path, target_file_name)
            os.rename(old_path, new_path)
    return pd.read_csv(new_path)
    

def extract_column_titles(dataframe, name_keywords, number_keywords):
    """
    Extract column titles related to names and numbers from a DataFrame.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame containing the data.
    - name_keywords (list): List of keywords indicating name-related columns (default is ['name']).
    - number_keywords (list): List of keywords indicating number-related columns (default is ['phone', 'number']).

    Returns:
    - list: List containing column titles related to names and numbers.
    """
    cols = list(dataframe.columns)

    names_numbers_col_title = []
    for col in cols:
        if any(keyword in col.lower() for keyword in name_keywords) and 'unname' not in col.lower():
            names_numbers_col_title.append(col)
        if any(keyword in col.lower() for keyword in number_keywords):
            names_numbers_col_title.append(col)

    return names_numbers_col_title

def extract_names_numbers(dataframe, name_column, number_column):
    """
    Engineer data by formatting names and numbers in the specified columns.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - name_column (str): The name-related column title.
    - number_column (str): The number-related column title.

    Returns:
    - tuple: Tuple containing formatted names and numbers.
    """
    # Extract Names
    names = [name.title().replace(' ', '%20') for name in dataframe[name_column]]

    # Extract Numbers and add country code
    numbers = dataframe[number_column].astype('str').apply(lambda x: f'91{x[-10:]}')
    
    # Check if total digits of a number is not 12
    assert all(len(number) == 12 for number in numbers), "Total digits of a number should be 12."

    return names, numbers

def send_whatsapp_messages(numbers, 
                           names, 
                           message_text, 
                           continue_to_chat_button_loc, 
                           dist_continue_chat_to_use_whatsapp_web,
                           initial_wait_duration,
                           whatsapp_loading_duration,
                           final_wait_duration):
    """
    Send WhatsApp messages to a list of phone numbers.

    Parameters:
    - numbers (list): A list of formatted phone numbers.
    - names (list): A list of names corresponding to the phone numbers.
    - message_text (str): The text of the message to be sent.
    - continue_to_chat_button_loc (tuple): Coordinates of the "Continue to Chat" button on the WhatsApp page.
    - dist_continue_chat_to_use_whatsapp_web (int): Distance from the "Continue to Chat" button to the "Use WhatsApp Web" button.
    - initial_wait_duration (int): Initial wait duration in seconds before interacting with the page.
    - whatsapp_loading_duration (int): Wait duration in seconds after clicking "Use WhatsApp Web" for the WhatsApp page to load.
    - final_wait_duration (int): Wait duration in seconds after sending the message before closing the WhatsApp tab.

    Note:
    - The function opens a new Chrome tab for each phone number, loads WhatsApp, sends the specified message, and then closes the tab.
    - Coordinates for button clicks and wait durations are configured for the specific layout and loading times of the WhatsApp Web page.
    - Ensure that the provided coordinates match the layout of the WhatsApp Web page to enable accurate interaction.
    """
    for i in range(len(numbers)):
        text = f"Hello%20{names[i]}%2C%0A%0A{message_text}"
        link = f"https://wa.me/{numbers[i]}?text={text}"

        # Load WhatsApp on Chrome
        os.system(f"start chrome {link}")
        time.sleep(initial_wait_duration)
        
        # After waiting, click on Continue to Chat Button
        pyautogui.click(x=continue_to_chat_button_loc[0], y=continue_to_chat_button_loc[1])
        time.sleep(initial_wait_duration)
        
        # After waiting, click on Use WhatsApp Web Button
        pyautogui.click(x=continue_to_chat_button_loc[0], y=continue_to_chat_button_loc[1]+dist_continue_chat_to_use_whatsapp_web)
        time.sleep(whatsapp_loading_duration)

        # After waiting, hit enter to send the message written via code
        pyautogui.press('enter')
        time.sleep(final_wait_duration)

        # After sending the message, close the WhatsApp tab from the Chrome browser
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(final_wait_duration)

def url_encode_text(text):
    """
    Encode the given text using urllib.parse.quote.

    Parameters:
    - text (str): The text to be encoded.

    Returns:
    - str: The encoded text.
    """
    return urllib.parse.quote(text)