import os

def DisplayContent(fileName):
    file = open(fileName, "r")
    content = file.read()
    print(content)
    file.close()

def main():
    fileName=input("Enter the name of file: ")
    ret=os.path.exists(fileName)
    if ret==False:         
        print("There is no such file")
    else:
        DisplayContent(fileName)    
    
if __name__=="__main__":
    main()  
    