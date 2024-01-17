# def greeting():
#     print("Hello there")
#     print("Welcome abroad")
    
# greeting()

# #with parameters and arguments
# def greeting(first_name , second_name):
#     print(f"Hello {first_name} {second_name}")
#     print("Welcome abroad")
    
# greeting("John" , "Hamedan")    


# def greet(name):
#     print(f"Hi {name}")
    
# print(greet("Mosh"))

# def increment(number , by):
#     return number + by

# print(increment(2 ,1))

# #default argument
# def increment(number , by=1):
#     return number + by

# print(increment(2))


# #number of arguments
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print(multiply(2,3,5,6,7))

# #placing multiple keys
# def save_user(**user):
#     print(user)
    
# save_user(id=1, name="John", age = 22)

# #using bracket notattion to specify a key       
# def save_user(**user):
#     print(user["name"])
    
# save_user(id=1, name="John", age = 22)  

# fixbuzz
# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return "fizz_buzz"
    
#     if input % 3 == 0:
#         return "fizz"
    
#     if input % 5 == 0:
#         return "buzz"
    
    
# print(fizz_buzz(15))

# def main():
#     a = age()
#     n = name()
#     t = temp()
#     s = school()
#     print(f'My name is {n}, i am {a} years old and i go to {s} .The temperaure here is {t} degree celsius.')
    
# #prompt for age 
# def age():
#     return input("Enter your age: ")
    
    
# #prompt for name
# def name():
#     return input("What's your name: ")
    
    
# #prompt for temp
# def temp():
#     return eval(input("Enter the temperature"))
    
    
# #prompt for school
# def school():
#     return input("Where do you go for school: ")
    
# main()







# age = int(input("What's your age: "))

# if age <=12:
#     print("You are a child")
    
# elif age <=19:
#     print("You are a teenager")
    
# elif age <= 25:
#     print("You are a young man")
    
# elif age > 25:
#     print("You are a mature man")




