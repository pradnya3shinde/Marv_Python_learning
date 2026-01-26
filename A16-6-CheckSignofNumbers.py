 
def CheckSign(number):    
        if number == 0:
            print("Zero")
        elif number>0:
            print("Positive Number")
        else:
            print("Negative Number")
                 

def main():
    no=int(input("Enter number: "))
    CheckSign(no)
    


if __name__=="__main__":
    main()