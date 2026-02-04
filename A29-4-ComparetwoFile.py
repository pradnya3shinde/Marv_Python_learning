import os
import sys

def CompareFileContent(source_file,destFile):
    with open(source_file, "rb") as f1, open(destFile, "rb") as f2:
        if f1.read() == f2.read():
            print("Success")
        else:
            print("Failure")

def main():
    if len(sys.argv) != 3:
        print("Invalid arguments!!")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2] 

    CompareFileContent(file1,file2)
    
if __name__=="__main__":
    main()  

import sys




