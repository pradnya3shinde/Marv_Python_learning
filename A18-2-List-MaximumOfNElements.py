def MaximumofNElemnts(no):
    lst=[]
    for i in range(no):
        lst.append(int(input("Enter number:")))

    max=lst[0]   
    for j in lst:
         if j > max:
            max = j
    print("Max. of list elements: ",max)    


def main():
    n = int(input("Enter how many number you want to enter: "))
    MaximumofNElemnts(n)
    

if __name__=="__main__":
    main()