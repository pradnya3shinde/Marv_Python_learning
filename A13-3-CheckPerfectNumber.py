import AssignmentLibrary

def checkPerfectNumber(number):  
    sum_div = 0

    for i in range(1, number):
        if number % i == 0:
            sum_div += i

    if sum_div == number:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

def main():
    no = int(input("Enter a number: "))
    checkPerfectNumber(no)
    

if __name__=="__main__":
    main()