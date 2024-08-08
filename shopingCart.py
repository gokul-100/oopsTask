#Create a class representing a shopping cart. Which include methods for adding items ,
# removing items , total items and total price
class shoppingcart:
    def __init__(self) -> None:
        self.cart={
            "shoe":500,
            "watch":1000,
            "bag":700,
            "notebook":100
            
        }
    
    def additems(self):
        item=input("enter the item name to add: ")
        self.cart[item]=int(input("enter the price: "))
        print()
        
    def removeItem(self):
        item_name=input("enter the item name to remove : ")
        if item_name in self.cart.keys():
            self.cart.pop(item_name)
        
        print("item removed..")
        
    def totalitem(self):
        print(f'toatl item present in the list {len(self.cart)}')
        
        
    def totalprice(self):
        sum=0
        for item in self.cart.keys():
            sum=sum+self.cart[item]
        print(f'toatl price in the cart is {sum}')
        


def main():
    obj1=shoppingcart()
    print(obj1.cart)
    obj1.additems()
    print(obj1.cart)
    obj1.removeItem()
    print(obj1.cart)
    obj1.totalitem()
    obj1.totalprice()

if __name__=="__main__":
    main()