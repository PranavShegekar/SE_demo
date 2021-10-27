# Name: Aaditya Cholayil
# Roll no.: CEB414
# Aim: Write a menu-driven program to demonstrate the use of list in python.
#      i) Put Even and Odd elements into Two Different Lists.
#     ii) Merge and sort the two lists.
#    iii) Update the first element with X value and delete the middle element of the list.
#     iv) Find max and min elements from the list.
#      v) Add N names into the existing number list and check if word python is present in the list.

even = [] 
odd = []  
merge = []

def takeInput():
    len=int(input('Number of elements: '))
    for i in range(1,len+1):
        n=int(input('{}: '.format(i)))
        if(n%2==0):
            even.append(n)
        else:
            odd.append(n)

def mergeAndSort():
    for i in even:
        merge.append(i)
    for i in odd:
        merge.append(i)
    if(len(merge)!=0):
        merge.sort()
        print('After Merging and Sorting:',merge)
    else:
        print('Both lists are empty')

def updateFirst():
    ch=int(input(menu2))
    n=int(input('Enter Number: '))
    if(ch==1):
        even.pop(0)
        even.insert(0, n)
        print('Updated List:', even)
    elif(ch==2):
        odd.pop(0)
        odd.insert(0, n)
        print('Updated List:', odd)
    elif(ch==3):
        merge.pop(0)
        merge.insert(0, n)
        print('Updated List:', merge)
    else:
        print('Enter a valid input')

def deleteMiddle():
    ch=int(input(menu2))
    if(ch==1):
        print(even.pop(int(len(even)/2)), 'was deleted')
        print('Updated List:', even)
    elif(ch==2):
        print(odd.pop(int(len(odd)/2)), 'was deleted')
        print('Updated List:', odd)
    elif(ch==3):
        print(merge.pop(int(len(merge)/2)), 'was deleted')
        print('Updated List:', merge)
    else:
        print('Enter a valid input')

def minMax():
    ch=int(input(menu2))
    if(ch==1):
        print('Min: {}\nMax: {}'.format(min(even), max(even)))
    elif(ch==2):
        print('Min: {}\nMax: {}'.format(min(odd), max(odd)))
    elif(ch==3):
        print('Min: {}\nMax: {}'.format(min(merge), max(merge)))
    else:
        print('Enter a valid input')

def addMultipleAndSearchPython():
    ch=int(input(menu2))
    n=int(input('Enter number of elements: '))
    print('Enter elements: ')
    if(ch==1):
        for i in range(1,n+1):
            even.append(input('{}: '.format(i)))
        print('After adding: ',even)
        if 'python' in even:
            print('Python found.')
        else:
            print('Python not found.')
    elif(ch==2):
        for i in range(1,n+1):
            odd.append(input('{}: '.format(i)))
        print('After adding: ', odd)
        if 'python' in odd:
            print('Python found.')
        else:
            print('Python not found.')
    elif(ch==3):
        for i in range(1,n+1):
            merge.append(input('{}: '.format(i)))
        print('After adding: ', merge)
        if 'python' in merge:
            print('Python found.')
        else:
            print('Python not found.')
    else:
        print('Enter a valid input')

def printAll():
    print('Even:',even)
    print('Odd:',odd)
    print('Merge:',merge)

menu2='''
Select the list:
1. Even List
2. Odd List
3. Merged List
Choice: '''

menu='''
---------List Operations---------
1. Take input
2. Merge and sort the two lists
3. Update first element
4. Delete middle element
5. Min and Max
6. Add N elements and check if python in list
7. Print all lists
8. Exit
Choice: '''

while(True):
    ch  = int(input(menu))
    if(ch==1):
        takeInput()
    elif(ch==2):
        mergeAndSort()
    elif(ch==3):
        updateFirst()
    elif(ch==4):
        deleteMiddle()
    elif(ch==5):
        minMax()
    elif(ch==6):
        addMultipleAndSearchPython()
    elif(ch==7): 
        printAll()
    elif(ch==8): 
        break
    else:
        print('Enter a valid input')
