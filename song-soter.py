import os

# Get the current directory where the script is located
folder_path = os.getcwd()

# Get all MP3 files in the directory
mp3_files = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]

# Sort files to maintain order (optional)
mp3_files.sort()

# Rename files
for index, file_name in enumerate(mp3_files, start=1):
    old_path = os.path.join(folder_path, file_name)
    new_path = os.path.join(folder_path, f"song{index}.mp3")
    os.rename(old_path, new_path)

print("Renaming completed successfully!")
