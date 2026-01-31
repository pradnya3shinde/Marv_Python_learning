class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        try:
            radius = float(input("Enter the radius of the circle: "))
            self.Radius = radius
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
            self.Accept()  

    def CalculateArea(self):       
        self.Area = Circle.PI * (self.Radius ** 2)

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("-" * 30)
        print(f"Radius: {self.Radius}")
        print(f"Area: {self.Area}")
        print(f"Circumference: {self.Circumference}")
        print("-" * 30)

circle1 = Circle()
circle1.Accept()
circle1.CalculateArea()
circle1.CalculateCircumference()
circle1.Display()

circle2 = Circle()
circle2.Accept()
circle2.CalculateArea()
circle2.CalculateCircumference()
circle2.Display()