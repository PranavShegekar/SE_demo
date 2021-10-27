# Name: Aaditya Cholayil
# Roll no.: CEB414
# Aim: Write a menu-driven program to demonstrate the use of a dictionary in python
#      a) Create a key/value pair dictionary
#      b) Update/concatenate and delete the item of the existing dictionary
#      c) Find a key and print its value
#      d) Map two list into a dictionary

d1={}

def newDict():
    dict={}
    n=int(input('Enter number of values: '))
    for i in range(0,n):
        key=input('Enter key: ')
        value=input('Enter value: ')
        dict.update({key: value})
    return dict

def dictUpdate():
    if d1!={}:
        key=input('Enter key: ')
        if key in d1:
            value=input('Enter new value: ')
            d1[key]=value
            print('Dictionary after updating:',d1)
        else:
            print('Key not found in Dictionary')
    else:
        print('Dictionary empty')

def dictDelete():
    if d1!={}:
        key=input('Enter key to be deleted: ')
        if key in d1:
            print(d1.pop(key), 'was deleted')
            print('Dictionary after deleting:',d1)
        else:
            print('Key not found in Dictionary')
    else:
        print('Dictionary empty')

def dictConc():
    print('Second Dictionary:')
    d2=newDict()
    d1.update(d2)
    print('After Concatenation:',d1)

def dictSearch():
    if d1!={}:
        key=input('Enter key: ')
        if key in d1:
            print('{}:{}'.format(key, d1[key]))
        else:
            print('Key not found in Dictionary')
    else:
        print('Dictionary empty')

def dictMap():
    keys=[]
    values=[]
    d1.clear()
    n=int(input('Enter number of values: '))
    for i in range(0,n):
        keys.append(input('Enter key: '))
        values.append(input('Enter value: '))
    print('Key list:', keys)
    print('Value list:', values)
    d2=dict(zip(keys, values))
    d1.update(d2)
    print('After Mapping:',d1)

menu='''
---------------DICTIONARY---------------
1. Enter dictionary
2. Update existing item in dictionary
3. Delete an item in dictionary
4. Concatenate with another dictionary
5. Search and print value using key
6. Map two list into dictionary
7. Exit'''

# Driver code
while(True):
    print(menu)
    choice=int(input('Enter choice: '))
    if(choice==1):
        d1=newDict()
        print('Dictionary:',d1)
    elif(choice==2):
        dictUpdate()
    elif(choice==3):
        dictDelete()
    elif(choice==4):
        dictConc()
    elif(choice==5):
        dictSearch()
    elif(choice==6):
        dictMap()
    elif(choice==7):
        break
