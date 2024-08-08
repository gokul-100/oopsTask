# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user’s information. Make another method called greet_user() that prints 
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.
class User:
    def __init__(self) -> None:
        self.__firstname=""
        self.__lastname=""
        self.__city=""
        
    def setdetails(self,fname,lname,city):
        self.__firstname=fname
        self.__lastname=lname
        self.__city=city
        
    def getdetails(self):
        print(f'firstname\t lastname\t city')
        print(f'{self.__firstname}\t      {self.__lastname}\t     {self.__city}')
        
    def greet(self):
        print(f'hi {self.__firstname}{self.__lastname} welcome to the world of coding...')
        
gokul=User()
gokul.setdetails("gokul","kannan","dharmapuri")
gokul.getdetails()
print("*"*100)
gokul.greet()