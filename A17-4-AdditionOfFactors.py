
def AdditionOfFactors(no):
    addition=0
    for i in range(1, no ):
        if no % i == 0:
            addition+=i
    print("Addition Of Factors: ",addition)     

def main():
    no = int(input("Enter a number: "))
    print("Factors of given number:")
    AdditionOfFactors(no)
    

if __name__=="__main__":
    main()