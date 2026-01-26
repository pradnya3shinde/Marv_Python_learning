 
def Add(no1,no2):    
       return no1+no2;
                 

def main():
    no1=int(input("Enter number: "))
    no2=int(input("Enter number: "))
    ret=Add(no1,no2)
    print("Addition: ", ret)


if __name__=="__main__":
    main()