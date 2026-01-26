def MinimumofNElemnts(no):
    lst=[]
    for i in range(no):
        lst.append(int(input("Enter number:")))

    min=lst[0]    
    for j in lst:
         if j < min:
            min = j
    print("Min. of list elements: ",min)    


def main():
    n = int(input("Enter how many number you want to enter: "))
    MinimumofNElemnts(n)
    

if __name__=="__main__":
    main()