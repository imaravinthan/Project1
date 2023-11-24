import codecs
import os

readme = "README.md"
direc = os.listdir('./')
if os.path.exists(os.path.join(os.getcwd(),readme)):
    print("File is available")
    file_lines = open(readme,errors="ignore")

    for line in file_lines:
        print(line)
else:
    print("File is not available....")
