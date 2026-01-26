 
def CheckNum(number):    
        if number % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")
                 

def main():
    no=int(input("Enter number: "))
    CheckNum(no)
    


if __name__=="__main__":
    main()