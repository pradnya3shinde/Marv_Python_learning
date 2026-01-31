class BankAccount:
    ROI=10.5
    def __init__(self,name,amount):
        self.Name=name
        self.Amount=amount
             
    def Display(self):
        print(f"Name: {self.Name} Balance: {self.Amount}")
    
    def Deposit(self,dAmount):
        self.Amount+=dAmount
        print(f"Name: {self.Name} Balance: {self.Amount}")
    
    def Deposit(self,dAmount):
        self.Amount+=dAmount
        print(f"Name: {self.Name} Balance: {self.Amount}")
    def CalculateInterest(self,):
        Interest=(self.Amount*BankAccount.ROI)/100
        print(f"Interest: {Interest}")


obj=BankAccount("Lila",10000)
obj.Display()
obj.Deposit(5000)
obj2=BankAccount("Sai",1000)
obj2.Display()
obj2.Deposit(50000)
obj2.CalculateInterest()
