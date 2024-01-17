# d = {'cat': 'an small creature like a leopard' , 'donkey': 'mammal that carrys load'}

# # prompting for a word in the dictionary
# word = input("What's the word:")

# #printing the meaning of the word
# print(d[word])


# d = {'I':1, 'IV':4, 'V':5, 'X':10}

# # prompting user for the roman numeral
# number = input("Enter the number: ")

# # prompting for the loop of the qtn
# for i in range(1,3): 
#     print(d[number])

# def roman_number(number):
#     '''A function that prints the number'''
#     print(f"The number is {d[number]}")

# # prompting for the dictionary    
# d = {'I':1, 'IV':4, 'V':5, 'X':10}

# # prompting user for the roman numeral
# number = input("Enter the number: ")

# # prompting for the loop of the qtn
# for _ in range(3):
#     roman_number(number)
    
    
    
# #working with dictionary
# #prompting for the dictionary
# d = {'A':400 , 'B':200}

# # using in operator to find key
# letter = input("Enter the letter: ")

# # prompting for in operator
# for letter in d: 
#     print("The value is ",d[letter])

# else:
#     print("Not in dictionary")

# # looping dictionary

# #printing keys in dictionary
# for key in d:
#     print(key)
    
# # printing values in keys
# for key in d:
#     print(d[key])


# #finding all keysin dictionary that correspond to 100
# d = {'A':100 , 'B':200 , 'C':100}
# L = [x[0] for x in d.items() if x[1] ==100]




# fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
# dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
# fishdog = {**fish, **dog}
# print(fishdog)


# dict = {'a':'1', 'b':'2'}
# #prompting for keys
# print(dict.keys())

# #prompting for values
# print(dict.values())

# #prompting for both keys and values
# print(dict.items())




# dictionary = {'Hello': 1234, 'World': 5678}
# w = dictionary.get("whatever")
# x = dictionary.get("whatever", "nuh-uh")
# # print(w)
# print(x)




# mydict = {'a': [1, 2, 3], 'b': ['one', 'two', 'three']}
# mydict['a'].append(4)
# mydict['b'].append('four')




capitals = {'USA': 'Washington DC','India': 'New Delhi',"Russia": 'Moscow','China':'Beijing'}
# capitals.update("Germany": "Berlin")
# capitals.update("USA": "Detroit")
# capitals.popitem("China")
# capitals.clear()


keys = capitals.keys()
for key in capitals.keys():
    print(key)


values = capitals.values()
for value in capitals.values():
    print(value)
    
    
item = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")