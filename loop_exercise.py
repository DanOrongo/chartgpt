#prompting for a program that prints name 100 times
for i in range(100):
    print("Orongo Daniel")
    

#filling da screen horizontally and vertically with name    
for i in range(10):
    print("DAN" *10)


#prompting a program from 1 to 100 with name
for i in range(100):
    print(i+1,"Dan")
    
    
#prompting a program that prints integers 1 to 20 with their square
for i in range(1,21):
    print(i , "---",i*i)
    

#prompting a prgram that loops backwards
for i in range(100,0,-2):
    print(i)



#prompting for name of user
name = input("What's your name:")
qtn = int(input("Enter number of times to be printed:"))
for i in range(qtn):
    print(name)
    
    
#using loop in def        
def appreciate_user(name):
    """a function that appreciates the user"""
    print("Thank you for shopping with us " + name)
    
#prompting for user's name
name = input("Enter your name: ")
    
#using loop to call the fuction several times
for i in range(5):
    appreciate_user(name)   

