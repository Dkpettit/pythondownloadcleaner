import os
import glob

file_path="C:/Users/User/Downloads/"
target_directory = os.listdir(file_path)
print(target_directory)
pattern = "*.jpg"

pattern1 = ".jpg"

for item in target_directory:
    file_name, file_extension = os.path.splitext(item)
    if file_extension in {pattern1}:
        print(item + " will be deleted.")
    else:
        print(item + " does not meet the requirements.")

for item in glob.iglob(os.path.join(file_path, pattern)):
    if os.path.isfile(item):
        os.remove(item)
        print(item + " has been removed./n")
    else:
        print(item + " does not meet the requirements.")





