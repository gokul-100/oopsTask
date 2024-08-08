# 9-1. Restaurant: Make a class called Restaurant. The init() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
# different instances from the class, and call describe_restaurant() for each 
# instance.




class Restarunt:
    def __init__(self,restaurant_name,cusine_type,) -> None:
        self.restaurant_name=restaurant_name
        self.cusine_type=cusine_type
        self.isopen=True
        
    def describe_retaurant(self):
        print("####Restaurant Details####")
        print(f'restaurant name {self.restaurant_name}')
        print(f'cousine type {self.cusine_type}')
        
    def open_restarunt(self):
        if self.isopen:
            print("now open")
        else:
            print("ooh! closed..")
            
class RRHotel(Restarunt):
    def __init__(self, restaurant_name, cusine_type,isopen) -> None:
        super().__init__(restaurant_name, cusine_type)
        self.isopen=isopen
class Atticafe(Restarunt):
    def __init__(self, restaurant_name, cusine_type,isopen) -> None:
        super().__init__(restaurant_name, cusine_type)
        self.isopen=isopen
class crescent(Restarunt):
    def __init__(self, restaurant_name, cusine_type,isopen) -> None:
        super().__init__(restaurant_name, cusine_type)
        self.isopen=isopen
            
rr=RRHotel("salem RR hotel","south indian",False)
atticafe=Atticafe("Atticafe","classic indian food",False)
Crescent=crescent("crescent night time Biriyani","Indian food",True)
print("-"*100)
rr.describe_retaurant()
rr.open_restarunt()
print("-"*100)
atticafe.describe_retaurant()
atticafe.open_restarunt()
print("-"*100)
Crescent.describe_retaurant()
Crescent.open_restarunt()      