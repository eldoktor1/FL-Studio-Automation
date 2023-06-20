import os
import shutil
import zipfile
import time
import pyautogui

def zip_loop_packages():
    # Prompt the user for the input folder path
    input_folder = input("Enter the input folder path: ")

    # Prompt the user for the output folder path
    output_folder = input("Enter the output folder path: ")

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all FL Studio project files in the input folder
    project_files = [
        file for file in os.listdir(input_folder)
        if file.endswith('.flp')
    ]

    # Check if there are any project files
    if not project_files:
        print("No FL Studio project files found in the input folder.")
        return

    # Resume from the last processed project file
    last_processed_file = None
    resume_option = input("Do you want to resume from where you left off? (y/n): ")
    if resume_option.lower() == 'y':
        last_processed_file = input("Enter the name of the last processed project file: ")

    resume = last_processed_file is not None
    for project_file in project_files:
        if resume:
            if project_file != last_processed_file:
                continue
            else:
                resume = False

        project_name = os.path.splitext(project_file)[0]
        project_path = os.path.join(input_folder, project_file)
        loop_package_name = f'{project_name}.zip'
        loop_package_path = os.path.join(output_folder, loop_package_name)

        # Open the FL Studio project
        os.startfile(project_path)
        time.sleep(10)  # Wait for FL Studio to open (adjust the delay if needed)

        # Press Ctrl+Shift+S to save the project
        pyautogui.hotkey('ctrl', 'shift', 's')
        time.sleep(1)  # Wait for the save dialog to appear

        # Type the loop package name and press Enter
        pyautogui.typewrite(loop_package_path)
        pyautogui.press('enter')
        time.sleep(1)  # Wait for the project to be saved as a loop package

        # Close the FL Studio project
        pyautogui.hotkey('alt', 'f4')
        time.sleep(1)  # Wait for the confirmation dialog (if prompted)
        pyautogui.press('enter')
        time.sleep(1)  # Wait for FL Studio to close

        print(f'Loop package created: {loop_package_name}')

        # Prompt the user to quit or continue
        choice = input("Enter 'q' to quit or any other key to continue: ")
        if choice.lower() == 'q':
            break

# Run the zip_loop_packages function
zip_loop_packages()

