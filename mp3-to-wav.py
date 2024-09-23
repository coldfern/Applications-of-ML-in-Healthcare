from pydub import AudioSegment
import os

def convert_mp3_to_wav(folder_path):
    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".mp3"):
            mp3_file_path = os.path.join(folder_path, file_name)
            wav_file_path = os.path.join(folder_path, file_name.replace(".mp3", ".wav"))

            # Load the mp3 file
            audio = AudioSegment.from_mp3(mp3_file_path)

            # Export as wav file
            audio.export(wav_file_path, format="wav")
            print(f"Converted {file_name} to {wav_file_path}")

folder_path = "your/folder/path"  # Replace with your folder path
convert_mp3_to_wav(folder_path)
