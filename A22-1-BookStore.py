class BookStore:
    NoOfBooks=0
    def __init__(self,name,author):
        self.Name=name
        self.Author=author
        BookStore.NoOfBooks+=1
             
    def Display(self):
        print(f" {self.Name} by {self.Author} No of Books: {self.NoOfBooks}")

obj=BookStore("Linux System programming","Rovert love")
obj.Display()

obj2=BookStore("C programming","Dennies Richie")
obj2.Display()
