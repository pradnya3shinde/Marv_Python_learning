def AdditionofNElemnts(no):
    lst=[]
    for i in range(no):
        lst.append(int(input("Enter number:")))
    total=0    
    for j in lst:
        total+=j
    print("Addition of list elements: ",total)    


def main():
    n = int(input("Enter how many number you want to enter: "))
    AdditionofNElemnts(n)
    

if __name__=="__main__":
    main()