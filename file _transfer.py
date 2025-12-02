import shutil

print("\n--- FILE TRANSFER APP ---")

src = input("Enter source file path: ")
dst = input("Enter destination folder path: ")

try:
    shutil.copy(src, dst)
    print("\nFile copied successfully!")
except:
    print("\nError: File not found or invalid path!")
