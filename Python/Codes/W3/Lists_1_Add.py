Foods = ['Strogonoff', 'Ratattuile', 'Hamburger']

Other_foods = ['Pizza', 'Lasanha', 'Beans']

#Foods[1] = "Lasanha" # This replaces (Ratattuile) for (Lasanha)

#Foods[1:2] = ['Lasanha', 'Ratattuile'] # This replaces (Ratattuile) for ['Lasanha', 'Ratattuile']

#Foods[1] = ['Lasanha', 'Ratattuile'] # This replaces (Ratattuile) for ['Lasanha', 'Ratattuile'] (A list inside another list)

#Foods.insert(2, "watermelon") # This inserts (watermelon) before 2

#Foods.append("orange") # This inserts (orange) at the end

Foods.extend(Other_foods) # This extends the list by the other list

print(Foods)