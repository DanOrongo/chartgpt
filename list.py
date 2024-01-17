# #prompting a list
# L = eval(input("Enter a list: "))
# print(L)

# #using the in operator
# if 2 in L:
#     print("The number 2 is in the list")
    
# if 0 not in L:
#     print("The list does not contain 0")
    
# #using loop
# for i in range(len(L)):
#     print(L[i])

# #prompting a list of 50 random numbers between 0 and 100
# from random import randint
# L = []
# for i in range(50):
#     L.append(randint(1,100))


#iterating over a list
# list = ['spoons','plates','knives']
# for item in list:
#     print(item)

# '''getting position for each item at the same time'''
# for (index,item) in enumerate(list):
#     print('The item in position {} is {}'.format(index, item))

# for item in list:
#     if item == 'spoon':
#         del list[0]
        
# print(item)


# '''checking presence of an item in a list'''
# lst =['test', 'twest','tweast','treast']
# all(lst)

# '''generators'''
# vals = [1,2,3,4]
# any(val> 12 for val in vals)
# any((val*2) > 6 for val in vals)




#Concatenate and Merge lists
# alist = ['a1','a2','a3']
# blist = ['b1','b2','b3']

# for a, b in zip(alist, blist):
#     print(a,b)
    

# import itertools
# alist = ['a1','a2','a3']
# blist = ['b1','b2','b3']
# clist = ['c3']

# for a, b, c in itertools.zip_longest(alist, blist, clist):
#     print(a,b,c)




# L = [2,4,5,6,7,10]
# for i in range(len(L)): 
#     print(L[i])
    
# for item in L:
#     print(item)





# L = [2,3,4,5,6,7,8,10,65,97]
# count = 0
# for item in L:
#     if item > 50:
#         count = count + 1
        
#     print(count)
    
    
    
# frequencies = []
# for i in range(1,101):
#     frequencies.append(L.count(i))




# from random import shuffle
# players = ['Joe', 'Bob', 'Sue', 'Sally']
# shuffle(players)
# for p in players:
#     print(p, 'it is your turn.')
    
#code to play the game goes here..
    
    
    
    

# from string import punctuation
# s = input('Enter a string: ')
# for c in punctuation:
#     s = s.replace(c, '')
# s = s.lower()
# L = s.split()
# word = input('Enter a word: ')
# print(word, 'appears', L.count(word), 'times.')


