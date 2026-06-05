import tkinter as tk

root = tk.Tk()
root.title('How to make coffee')

recipe_text = '''Classic Coffee Recipe
Ingredients:
1 cup of water
2 tablespoons of ground coffee (or one coffee pod if using a single-serve coffee maker)
Milk or cream (optional)
Sugar or sweetener (optional)
Instructions:
Boil Water: If using a drip coffee maker, fill the reservoir with water and turn it on. If using a kettle, boil 1 cup of water.

Prepare Coffee:

Drip Coffee Maker: Place a coffee filter in the basket and add 2 tablespoons of ground coffee.
Single-Serve Coffee Maker: Insert a coffee pod into the machine.
Brew:

Drip Coffee Maker: Pour the boiled water over the coffee grounds (if not using a machine) and let it drip through.
Single-Serve Coffee Maker: Follow the machine's instructions to brew a cup of coffee.
Serve:

Pour the brewed coffee into a mug.
Add milk or cream if desired.
Sweeten with sugar or sweetener to taste.
Enjoy: Stir well and enjoy your coffee!'''

label = tk.Label(root, text=recipe_text, justify=tk.LEFT)
label.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()