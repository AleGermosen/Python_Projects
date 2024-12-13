### Text editor app

# User input to create or open text file
# Display if the file exists
# While loop waiting for the file to be saved and exit the program
# User input to save the file or enter new text
# Display when file is saved and program is terminated

import os
from pathlib import Path

def text_editor_app():
    file_name = input("Enter the filename to open or create: ")
    if os.path.exists(Path(file_name)):
        print("File exists!")
        with open(file_name, "a") as file:
            print("Enter SAVE on a new line to save and exit.\nEnter your text:")
            while True:
                user_text = input()
                if (user_text == "SAVE"):
                    file.close()
                    print(f"File {file_name} saved.")
                    break
                else:
                    file.write(user_text)
                    file.write("\n")
    else:
        print("File does not exist.")
        with open(file_name, "w") as file:
           pass