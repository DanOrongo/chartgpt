s = "simplilearn"
for i in s:
    print(i)
    
#enforcing the end function
s = "simplilearn"
for i in s:
    print(i , end= '*')
    

# using for list in loop
programming = ["java" , "python" , "HTML" , "RUBY"]
for iter in programming:
    print(iter)
    

#finding average of a list of numbers
list_num = [20, 30, 50, 45 , 60]
sum = 0
for i in list_num:
    sum = sum + i
    print("sum =" ,sum)
    print('Average is ' , sum/len(list_num))
    
    
    
#for loop using a tuple
num = (20,43,56,78,95)
sum = 0
for i in num:
    sum = sum + i 
    print(sum)
#when print is not indented
print(sum)


#program to print multiplication table of a number
n = int(input("Enter the number: "))
for i in range(1,11):
    mul = n*i
    print(n,'*',i, "=" ,mul)
    
    
#Nested for loop
companies = ("Google","Microsoft","Apple","Samsung")
for i in companies:
    print("We will display every letter in "+i)
    for letter in i:
        print(letter)
        
        
#break
for i in range(1,10):
    if (i==6):
        break
    print(i)
    
    
#continue
for i in range(1,10):
    if (i==6):
        continue
    print(i)


#program to display total goals a player has scored
player_name = "Ronaldo"
goals = {"Ronaldo": 2 , "Gernacho": 1, "Fernandes": 4}
for player in goals:
    if player == player_name:
        print(goals[player])
        break
else:
    print("No player with that name found")    
        
        


def main():
    meow(5)

def meow(n):
    for i in range(n):
        print("meow")
        
main()        