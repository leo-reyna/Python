import os

def list_files_in_folder(folder_path):
    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")

        # Get a list of filenames in the specified folder
        filenames = os.listdir(folder_path)

        # Print the list of filenames
        print(f"Files in {folder_path}:")

        for filename in filenames:
            print(filename)

        return filenames

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Get folder path from the user
    folder_path = input("Enter the folder path: ")

    # Call the function to list files in the folder
    filenames = list_files_in_folder(folder_path)

    # Use the filenames list as needed in the rest of your script

if __name__ == "__main__":
    main()
