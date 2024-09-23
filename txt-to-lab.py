import os

def convert_txt_to_lab(folder_path):
    # Get list of all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file has a .txt extension
        if filename.endswith('.txt'):
            # Construct full file path
            txt_file = os.path.join(folder_path, filename)
            # Replace the .txt extension with .lab
            lab_file = os.path.join(folder_path, filename.replace('.txt', '.lab'))
            # Rename the file
            os.rename(txt_file, lab_file)
            print(f"Converted: {filename} to {filename.replace('.txt', '.lab')}")

folder_path = 'path_to_your_folder'  # Replace this with your folder path
convert_txt_to_lab(folder_path)
