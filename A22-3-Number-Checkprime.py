class NumberBehaviour:     
    def __init__(self,No):
        self.no=No
             
    def CheckPrime(self):
        if self.no <= 1:
            print("Not a Prime Number")
        else:
            for i in range(2, int(self.no**0.5) + 1):
                if self.no % i == 0:
                    print("Not a Prime Number")
                    break
                else:
                    print("Prime Number")
    
    def checkPerfectNumber(self):  
        sum_div = 0

        for i in range(1, self.no):
            if self.no % i == 0:
                sum_div += i

        if sum_div == self.no:
            print("Perfect Number")
        else:
            print("Not a Perfect Number")
            
       
    
    def Factors(self):
        print("Factore are: ")
        for i in range(1, self.no):
            if self.no % i == 0:
                print(i)

    def SumFactors(self):
        sum=0
        for i in range(1, self.no):
            if self.no % i == 0:
                sum+=i
        print("Sum of Factore is: ",sum)
    
         
       

no = int(input("Enter a number: "))
obj=NumberBehaviour(no)
obj.CheckPrime()
obj.checkPerfectNumber()
obj.Factors()
obj.SumFactors()
