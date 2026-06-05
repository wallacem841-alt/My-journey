import os

def clear_directory(directory):
    # Iterate through all items in the specified directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)  # Delete the file or symbolic link
            elif os.path.isdir(item_path):
                # Recursively clear the contents of the directory
                clear_directory(item_path)
        except Exception as e:
            print(f'Failed to delete {item_path}. Reason: {e}')

# Specify the directory path
directory = r"C:\Users\Usuario\Desktop\Wallace\Real Life"

# Clear the directory contents (files only, not directories)
clear_directory(directory)

print(f"All files in {directory} have been deleted.")