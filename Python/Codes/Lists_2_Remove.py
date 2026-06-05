Foods = ['Strogonoff', 'eggplant','zucchini', 'Ratattuile', 'Hamburger','Ratattuile']

Other_foods = ['Pizza', 'Lasanha', 'Beans']

Foods.remove('Ratattuile') # This remove the first ('Ratattuile')
Foods.pop(1) # This removes the index (1)
'''When it removes the index 1, the index 2 becomes the index 1 and so on'''
del Foods[1] # This also removes the index (1)

# del Foods # This deletes the list completely

# Foods.clear() # this clears the list's content

print(Foods)