import os
def createfile(filename):
    if (os.path.exists(filename)):
        print('filename already exists..')
    else:
        file_create=open(filename,'w')
    file_create.write(input("enter the text to add : "))
# text=input("enter the text to search: ")

def frequency(filename,text):
    file=open(filename,'r')
    if text in file.read():
        print("the text is present")
    else:
        print("text is not present..")

if __name__=="__main__":
    filename=input("enter the filname : ")
    createfile(filename)
    text=input("enter the txt to search : ")
    frequency(filename,text)
    
    
    