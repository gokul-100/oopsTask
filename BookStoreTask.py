class Bookstore:
    NoofBooks=0
    def __init__(self,name,author) -> None:
        self.name=name
        self.author=author
        Bookstore.NoofBooks+=1
        
    def display(self):
        print(f'name of the book',self.name)
        print(f'author of book',self.author)
        print(f'no of books',self.NoofBooks)
        
Obj1=Bookstore("Linux System Programming","Robert Love")

Obj1.display()

Obj2=Bookstore("c programing ","robert")
Obj2.display()