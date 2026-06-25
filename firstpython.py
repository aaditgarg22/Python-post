"""consedering a rectangle with side a and b

a=int(input("Enter the length of side a: "))
b=int(input("Enter the length of side b: "))
name='rectangle'
print ("The area of the", name, "is", a*b) 
print("The perimeter of the", name, "is", 2*(a+b))

#STRING OPERATIONS

str1 = input("Enter a string: ")
str= "aadit garg"\
print("The length of the string is: ", len(str1)) 
print (str.replace("a", "Q"))
print (str.capitalize())
print(str.count("garg"))
print(str.find("d"))
print(str.endswith("rg"))

#CONDITIONAL CODES

age= int(input("your age="))
if( age>=18):
    print("u are an adult")
else:
    print("u are not an adult")
    

#making a code that can tell wether a number is odd or even 

num=int(input('enter a number:'))

if( num%2==0):
    print("number is even")
else: 
    print("number is odd")    

#TAKING 3 NUMBERS FROM USER AND FINDING LARGEST AMONG THEM

a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))

if (a>b and a>c): 
    print(a ,"is the largest number")
elif(b>a and b>c):
    print(b ,"is the largest number")   
else:
    print(c ,"is the largest number")     

#CREATING A CODE TO CHECK WETHER A NUMBER IS MULTIPLE OF 7,9,OR NOT

number=int(input("enter your number"))

if(number%7==0):
    print("number is divisible by 7")
if(number%9==0):
    print("number is divisible by 9")    
else:
    print("number is neither divisible by 7 nor 9 ")    """