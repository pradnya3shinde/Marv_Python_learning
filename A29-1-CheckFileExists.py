import os

def main():
    fileName=input("Enter the name of file: ")
    ret=os.path.exists(fileName)
    if ret==False:         
        print("There is no such file")
    
if __name__=="__main__":
    main() 