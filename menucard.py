# 1) Create a menu_card list
# veg_starter = ['paneer 65','chilly paneer','veg crispy']
# 1) Display menu card
# 2)Add Starter in the menu card
# 3)Update Starter in the menu card
# 4)Remove Starter in the menu card

class menu:
    items_list=[]
    def __init__(self) -> None:
        self.item=""
        
    def add(self):
        noofitem=int(input("enter the noof items to add : "))
        for i in range(noofitem):
            self.item=input("enter the name of item to add : ")
            if self.item==' ':
                print("you must enter the item name to add ")
                return self.item
            else:
                menu.items_list.append(self.item)

                
    def remove(self):
            item=input("enter the item name to remove : ")
        # for i in range(0,len(self.items_list)):
            # if self.items_list[i]==item:
            if item in self.items_list:
                self.items_list.remove(item)
            else:
                print("item is not present in the list")
        
    def update(self):
        print(self.items_list)
        index=int(input("enter the item index to update : "))
        if index<=len(self.items_list) and index>0:
            self.items_list[index-1]=input("enter the name to update:  ")
            print("list updated successfully...")
        else:
            print("you enter the wrong index value....")
            self.update()
            
    def display(self):
        print("****details of items****")
        print("sno\t   item name")
        for i in range(0,len(self.items_list)):
            print(f'{i+1}\t   {self.items_list[i]}')
        
        


def main():
    obj1=menu()
    obj1.add()
    obj1.display()
    print("*"*100)
    obj1.update()
    obj1.display()
    print("*"*100)
    obj1.remove()
    obj1.display()


if __name__=="__main__":
    main()

