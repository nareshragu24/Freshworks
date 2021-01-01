import json
import threading
from threading import*

#Before run this code create a json file named "values.json" and enter one sample value like {"don@gmail.com": 100} 

keyval = dict()

def create():           #Create Function

    mail = input("Enter email id: ")

    with open("values.json", "r+") as f:       #To check whether the key is already present 
            data = json.load(f)
            if mail in data:
                print("Error: Mail id already exists")
                return

    num = int(input("Enter Mark: "))
    keyval[mail]=num
    


    if len(keyval)<(1024*1024*1020) and (int(num)<=(16*1024*1024)):         #To check the size of the file 
        with open("values.json", "r+") as f:
            data = json.load(f)
            data.update(keyval)
            f.seek(0)
            json.dump(data, f)
        print("**********CREATED**********")
    else:
        print("Error: Memory Limit exeeded")


def search():                       #Search Function
    mail = input("Enter mail id: ")
    with open("values.json", "r") as f:
        data = json.load(f)
    if mail in data:
        print("*********SUCCESSFULLY FOUND**********")
        print("Marks of the mail ",mail, " is",data[mail])
        print("\n")
    else:
        print("*********NOT FOUND***********")


def delete():                   #Delete function
    mail = input("Enter mail id: ")
    with open('values.json', 'r') as f:
        values = json.load(f)

    if mail in values:
        del values[mail]
        values.update()
        print("*********SUCCESSFULLY DELETED**********")
    else:
        print("Error: There is no such account")

    with open('values.json', 'w') as f:
        values = json.dump(values, f)


while True:
    print("Enter what you want to do")
    print("1.Create")
    print("2.Search")
    print("3.Delete")
    print("Type'N' to stop")
    x = int(input())
    if(x==1):
        create()
        #print("created")
    elif(x==2):
        search()
        #print("Searched")
    elif(x==3):
        delete()
        #print("deleted")
    else:
        print("enter valid input")


    