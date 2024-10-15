import os
import glob
import shutil

def clean_temp_files(directory):
    files = glob.glob(os.path.join(directory, '*.tmp'))
    for file in files:
        os.remove(file)
    print(f"Removed {len(files)} temporary files.")

def copy_file(source, destination):
    shutil.copy(source, destination)
    print(f"Copied {source} to {destination}.")

def delete_files_with_extension(directory, extension):
    files = glob.glob(os.path.join(directory, f'*{extension}'))
    for file in files:
        os.remove(file)
    print(f"Removed {len(files)} files with extension {extension}.")

def rename_files(directory, old_pattern, new_pattern):
    for filename in os.listdir(directory):
        if old_pattern in filename:
            new_name = filename.replace(old_pattern, new_pattern)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
    print(f"Renamed files matching {old_pattern} to {new_pattern}.")
