class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):       
            self.Value1 = float(input("Enter Value 1: "))
            self.Value2 = float(input("Enter Value 2: "))
        
    def Add(self):
        add=self.Value1 + self.Value2
        print(f"Addition is : {add}") 

    def Sub(self):
            sub=self.Value1 - self.Value2
            print(f"Substraction is : {sub}")  

    def Mult(self):
            mult=self.Value1 * self.Value2
            print(f"Multiplication is : {mult}")  

    def Div(self):
        if self.Value2 != 0:
            div= self.Value1 / self.Value2
            print(f"Division is : {div}")  

        else:
            print("Error: Cannot divide by zero.")

obj1=Arithmetic()
obj1.Accept()
obj1.Add()
obj1.Sub()
obj1.Mult()
obj1.Div()
print("-" * 30)
obj2=Arithmetic()
obj2.Accept()
obj2.Add()
obj2.Sub()
obj2.Mult()
obj2.Div()