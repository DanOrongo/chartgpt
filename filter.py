# def check_even(number):
#     if number % 2 ==  0:
#         return True
    
#     return False

# numbers = [1,2,3,4,5,6,7,8,9,10]

# # if an element passed to check_even() returns True, select it
# even_numbers_iterator = filter(check_even, numbers)

# # converting to list
# even_numbers = list(even_numbers_iterator)

# print(even_numbers)





# # Define a list of names
# names = ["John Smith", "Jane Doe", "Bob Johnson", "Alice Brown"]

# # Define a function to extract the last name from a full name
# def get_last_name(full_name):
#     return full_name.split()[-1]

# # Use the map() function to get a new list of last names
# last_names = list(map(get_last_name, names))

# # Print the new list of last names
# print(f"The last names are: {last_names}")





#Define a list of fruits
fruits = ["Malus domestica", 'Musa spp', 'Vitis vinifera']

#defining function to extract first name of the fruits
def genus(fruit):
    return fruit.split()[0]

#getting new list of genus
all_genus = list(map(genus, fruits))

#printing all the genus
print("The genus names are ",all_genus)