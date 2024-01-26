"""
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)"""



# Answer

# First create a list of your fav marvel super heroes.

heroes = ['spider man','thor','hulk','iron man','captain america']


#1. Length of the list

print("Answer 1:")
print(f"The length of the heroes list : {len(heroes)}")

print("")


#2. Add 'black panther' at the end of this list.

print("Answer 2:")
new_hero = 'black panther'
heroes.append(new_hero)
print(f"New list of heroes : {heroes}")

print("")


#3. You realize that you need to add 'black panther' after 'hulk',so remove it from the list first and then add it after 'hulk'

print("Answer 3:")

#remove 'black panther'
heroes.remove('black panther')

#add it after hulk
heroes.insert(3,'black panther')

print(f"Corrected list of heroes : {heroes}")

print("")


#4. Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code.

print("Answer 4:")
# In one line
heroes[1:3] = ['doctor strange']
print("New fav. ",heroes)

print("")


#5.Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

print("Answer 5:")
heroes.sort()
print("Sorted list :",heroes)

