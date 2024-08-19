# File Renamer Script

This Python script renames all files in a specified directory by adding a user-defined prefix followed by a sequential number. This can be particularly useful for organizing files, such as photos or documents, in a more systematic way.

## How It Works

1. **Importing the `os` Module:**
   - The script begins by importing the `os` module, which allows the script to interact with the operating system, particularly for file and directory operations.

2. **Function `rename_files(directory, prefix)`:**
   - This function takes two arguments:
     - `directory`: The path of the directory containing the files to be renamed.
     - `prefix`: The prefix you want to use for the new filenames.

3. **Listing Files in the Directory:**
   - `os.listdir(directory)` is used to get a list of all the files in the specified directory.

4. **Enumerating Over Files:**
   - The script uses a `for` loop with `enumerate(os.listdir(directory))` to loop through each file in the directory. `enumerate` provides both the index (`count`) and the filename (`filename`).

5. **Constructing New Filenames:**
   - For each file, a new name is constructed by combining the prefix with the count (which is converted to a string) and the original file extension:
     ```python
     dst = f"{prefix}_{str(count)}{os.path.splitext(filename)[1]}"
     ```
     - `os.path.splitext(filename)[1]` extracts the file extension (e.g., `.txt`, `.jpg`).

6. **Joining Paths:**
   - The script uses `os.path.join(directory, filename)` to create the full path to the original file (`src`) and the new file name (`dst`).

7. **Renaming Files:**
   - `os.rename(src, dst)` renames the file from its original name (`src`) to the new name (`dst`).

8. **User Interaction:**
   - The script uses `input()` to prompt the user to enter the directory path and the prefix for the new filenames.

9. **Executing the Function:**
   - If the script is run directly (i.e., not imported as a module), the code inside the `if __name__ == "__main__":` block is executed. This block gets the user inputs and calls the `rename_files` function with those inputs.

10. **Completion Message:**
    - After all the files have been renamed, the script prints `"Files renamed successfully!"` to indicate the process is complete.

## Example Use Case

Suppose you have a directory `/home/user/photos/` containing files like `image1.jpg`, `image2.jpg`, etc., and you want to rename them all with the prefix `holiday`. The script will rename the files to `holiday_0.jpg`, `holiday_1.jpg`, etc.

- **Input:**
  - Directory path: `/home/user/photos/`
  - Prefix: `holiday`
- **Output:**
  - The files in the directory will be renamed to `holiday_0.jpg`, `holiday_1.jpg`, etc.
 
## Requirements

- Python 3.x

No external libraries are required to run this program. It uses Python's built-in `os` module.

---

This script is particularly useful when you have a lot of files with arbitrary names and want to standardize their names with a consistent prefix and numbering.
