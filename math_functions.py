from math import sin, pi
print("Pi is roughly ",pi)
print("The value of sin(2) is ",sin(2))

# using built in math functions abs and round functions
# prompting for abs function
print(abs(-34.657))

#prompting for round function
print(round(345.746,2))


#prompting a program that generates 50 random integers between 3 and 6
from random import randint
x = randint(3,6)
print("The random number between 3 and 6 is " ,x)

# prompting a program that generates random number x and y
# prompting for x between 1 and 50
from random import randint
x = randint(1,50)

# prompting for y between 2 and 5
y = randint(2,5)

print("The random number between 1 and 50 is ",x)
print("The random number between 2 and 5 is ",y)

#prompting for  x
print("The value is " , x)


#prompting for random number between 1 and 10
from random import randint
x = randint(1,10)
print("The random number is " , x)

#prompting to print name x times
for i in range(x):
    print("My name is Dan")


#if statement
from random import randint
num = randint(1,10)

# prompting for the user's guess number
guess = eval(input("Enter your guese: "))

# prompting for if statement
if guess == num:
    print("yes, you got it")
    
else:
    print("Sorry, the number is " ,num)
    
    
    
# prompting user for length in centimeters
length = eval(input("Enter your length: "))
inch = (length*2.54)
if length<0:
    print("Invalid length")
    
elif length>1:
    print("The length in inches is ",inch)




#prompting user for temperature celsius
temp = eval(input("Enter your temperature in celsius: "))

# prompting for temperature
if temp<-273.15:
    print("Invalid temperature because it is below absolute zero")
    
elif temp==-273.15:
    print("This is the absolute temperature")
    
elif 0>temp or temp<-273.15:
    print("The temperature is below freezing")
    
elif temp==0:
    print("The temperature is at freezing point")
    
elif 0<=temp<=100:
    print("It is normal temperature")
    
elif temp==100:
    print("The teperature is at boiling point")
    
elif temp>100:
    print("The temperature is above boiling point")
    
    
# prompting for temperature                        
temp = eval(input("Enter your temperature: "))

# prompting the scale of the temperature
scale = input("Enter the respective scale: ")


#using if statement to print
# if scale is F:
#     print("The scale in celsius is " ,F = 9/5*temp)

# elif scale is C:
#     print('The scale in fahrenheit is ' ,C = 5/9*(temp-32))

