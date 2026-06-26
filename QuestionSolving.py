"""a=input("enter your 1st film: ")
b=input("enter your 2nd film: ")
c=input("enter your 3rd film: ")

list=[a,b,c]

print(list)"""

list=[1,2,3]
list2=[1,2,3,2,1]

listcopy=list2.copy()
listcopy.reverse()

if(listcopy==list2):
    print("palindrome")
else:
    print("not palindrome")

    
