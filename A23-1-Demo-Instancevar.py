class Demo:
    value=0
    def __init__(self,no1,no2):
        self.No1=no1
        self.No2=no2
             
    def fun(self):
        print(f" No1={self.No1} No2: {self.No2}")
    
    def gun(self):
        print(f" No1={self.No1} No2: {self.No2}")


obj=Demo(11,21)
obj2=Demo(51,101)

obj.fun()
obj.gun()

obj2.fun()
obj2.gun()
