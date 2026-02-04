import os
import sys

def CopyContent(fileName):
    destination_file = "new.txt"
    try:
        src=open(fileName, "r")
        dest=open(destination_file, "w")

        line = src.readline()
        while line:
            dest.write(line)
            line = src.readline()

        print("File copied successfully")
        print("Create Abc.txt and copy contents of", fileName, "into Abc.txt")

    except FileNotFoundError:
        print("Source file not found!")

def main():
    if len(sys.argv) != 2:
        return

    source_file = sys.argv[1]    
    CopyContent(source_file)
    
if __name__=="__main__":
    main()  
