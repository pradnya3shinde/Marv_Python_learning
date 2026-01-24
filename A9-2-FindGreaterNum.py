def chkGreater(no1,no2):
    if(no1>no2):
        print("Greater number is : ",no1)
    else:
        print("Greater number is : ",no2)

def main():
    no1=int(input("Enter 1st number: "))
    no2=int(input("Enter 2nd number: "))

    chkGreater(no1,no2)

if __name__ =="__main__": 
    main()   