# List all of this 
ingrediants = ['water', 'milk', 'black tea']
ingrediants.append('sugar')
print(f'Ingrediants are: {ingrediants}')
ingrediants.remove("water")
print(f'Ingrediants are: {ingrediants}')

spice_options = ['ginger', 'cardmom']
chai_ingredients = ['water', 'milk']


chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")
chai_ingredients.insert(2, "black tea")
print(f"chai: {chai_ingredients}")

# use pop function 

last_added = chai_ingredients.pop()
print(f'{last_added}')
print(f"chai: {chai_ingredients}")

# print(f'chai: {chai_ingredients.reverse()}') --> after reverse print the list 

chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")

# sort function

chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

# minimum and maximum function use 

sugar_level = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_level)}")
print(f"Minimum sugar level: {min(sugar_level)}")


# operator overloading
 
base_liquid = ['water', 'milk']
extra_flavour = ['ginger']


full_liqid_mix = base_liquid + extra_flavour
print(f"Liquid mix: {full_liqid_mix}")

strong_brew = ['black tea', 'tea', 'water'] * 3
print(f'String brew: {strong_brew}')


# from operator import itemgetter

raw_spice_data = bytearray(b"CINAMON")
raw_spice_data.replace(b'CINNA', B'CARD')
print(f'Bytes: {raw_spice_data}')


# 