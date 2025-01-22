import os
import shutil

print(os.getcwd())

mainFile = input("What file to copy from: ")
whereFile = input("Where do you want to copy the file: ")

shutil.copyfile(mainFile, whereFile)
