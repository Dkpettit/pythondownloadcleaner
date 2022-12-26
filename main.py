import os
import glob

file_path="C:/Users/User/Downloads"

pattern = "*.jpg"

def find_files(base, pattern):
    print(glob.glob(pattern))
    '''Return list of files matching pattern in base folder.'''
    return [n for n in glob.glob(pattern) if os.path.isfile(n) if
        os.path.isfile(os.path.join(base, n))]

target_files = find_files(file_path, pattern)

print(target_files)

for x in target_files:
    print(x)
    if os.path.isfile(x):
        os.remove(x)
        print("File has succesfully been deleted!")
    else:
        print("This file does NOT exist!!!")


