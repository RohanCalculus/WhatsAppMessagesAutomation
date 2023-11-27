# 📩 Automating WhatsApp messages to send them to different numbers!

### 🎯 **Aim**           
_This project is developed for [Spartificial](https://spartificial.com) to automate the process of sending invitations to students via WhatsApp for their programs and workshops._

### ⚙️ **How to Configure the Parameters in `config.py`**
1. _Change the `DIRECTORY_PATH` to the path where the student's CSV data is stored in your system_
2. _Use `mouse_coordinates.py` to configure your mouse location on WhatsApp screen_
3. _Update the `CONTINUE_TO_CHAT_BUTTON_LOC` according to your system after finding it from step 2_
4._Check the distance between the `Click to Continue` button and the `Use WhatsApp Web` button and change the `DIST_CONTINUE_CHAT_TO_USE_WHATSAPP_WEB` accordingly_
5. _Set up the time durations for `INITIAL_WAIT_DURATION`, `WHATSAPP_LOADING_DURATION`, and `FINAL_WAIT_DURATION` according to the power of your system_
6. _Change the `WHATSAPP_TEXT` based on the training program details to customize the reminder for students_
   
### ➡️ **Details of all the files**
1. _Use `config.py` to configure the parameters according to your system_
2. _Upload a `data.csv` file that has the data of student names and respective phone numbers_
3. _Use `mouse_coordintes.py` to configure your mouse location on WhatsApp screen_
4. _`utlity.py` has all the utility functions used in this project_
5. _`main.py` is the main file to run the project! Run it after configuring your mouse location and other parameters if required_

### 🤝 **Developer Details**
$\rightarrow$ **`Name:`** *Rohan Shah*           
$\rightarrow$ **`Message:`** *Reach out to me in case of any discussions over this repo or for any projects related to Python and AI/ML.*



