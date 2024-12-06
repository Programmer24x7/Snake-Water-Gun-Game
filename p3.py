import os

def list_directory_contents(path="."):
    """
    Prints the contents of the specified directory.

    Parameters:
    path (str): Path to the directory. Defaults to the current directory.
    """
    try:
        # Get the list of files and directories in the specified path
        contents = os.listdir(path)
        
        print(f"Contents of the directory '{os.path.abspath(path)}':")
        for item in contents:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print(f"[DIR]  {item}")
            else:
                print(f"[FILE] {item}")
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access the directory '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Specify the directory to list or leave it empty for the current directory
directory = input("Enter the directory path (leave blank for current directory): ").strip() or "."
list_directory_contents(directory)

