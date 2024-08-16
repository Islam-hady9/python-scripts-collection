import os

def rename_files(directory, prefix):
    for count, filename in enumerate(os.listdir(directory)):
        dst = f"{prefix}_{str(count)}{os.path.splitext(filename)[1]}"
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, dst)
        os.rename(src, dst)
    print("Files renamed successfully!")

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    prefix = input("Enter the new file name prefix: ")
    rename_files(directory, prefix)