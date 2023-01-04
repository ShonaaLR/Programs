1.	Print the days of the week with (1- 7)
         1-SUN, 2-MON......7- SAT	

PROGRAM:
a=int(input("Enter the integer:"))
if(a==1):
    print("sunday")
elif(a==2):
    print("Monday")
elif(a==3):
    print("Tuesday")
elif(a==4):
    print("Wednesday")
elif(a==5):
    print("Thursday")
elif(a==6):
    print("Friday")
elif(a==7):
    print("Saturday")
else:
    print("Enter the valid input")
    
OUTPUT:
Enter the integer: 4
Wednesday 



2.	Smallest of. three numbers

PROGRAM:

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if((num1<num2) and (num1<num3)):
    print("smallest",num1)
elif((num1<num1) and (num2>num3)):
    print("smallest",num2)
else:
    print("smallest",num3)
	


OUTPUT:
Enter first number:2
Enter second number:3
Enter third number:4
smallest 2
	


3.	Read a Character. if it is Lower , Print ** else print U
  
PROGRAM:

ch=input("Enter the character:")
if(ch>='a' and ch<='z'):
    print("**")
else:
    print("U")

OUTPUT:	
Enter the character: s
**




