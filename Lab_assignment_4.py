Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q.1
marks=float(input("Enter Marks: "))
if(marks<25):
    print(" Grade F ")
elif(marks>=25 and marks<45):
    print(" Grade E ")
elif(marks>=45 and marks<50):
    print(" Grade D ")
elif(marks>=50 and marks<60):
    print(" Grade C ")
elif(marks>=60 and marks<80):
    print(" Grade B ")
elif(marks>=80 ):   
    print(" Grade A ")
else:
    print(" ERROR ")


#Q.2
year = int(input("Enter a year: "))

if year % 4 == 0 :
    print(year ,"is a Leap Year")
elif year % 100 == 0 :
    print(year ,"is not a Leap Year")
elif year % 400 == 0 :
    print(year ,"is a Leap Year")
else :
    print(" ERROR ")


#Q.3
import random
for i in range(10):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    print(f"Question {i+1}:",end="")
    user_output = int(input(f"{num1}X{num2}="))
    if user_output == (num1*num2):
        print("Right!")
    else:
        print(f"Wrong.The right answer is {num1*num2}.")