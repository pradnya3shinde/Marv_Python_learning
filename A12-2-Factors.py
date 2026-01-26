
def Factors(no):
    for i in range(1, no):
        if no % i == 0:
         print(i)

def main():
    no = int(input("Enter a number: "))
    print("Factors of given number:")
    Factors(no)
    

if __name__=="__main__":
    main()