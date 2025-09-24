essential_spices = {"cardamon", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepp"}

# all spices 
all_spices = essential_spices | optional_spices
print(f'All spices : {all_spices}')

# common spices 
common_spices = essential_spices & optional_spices
print(f'common spices: {common_spices}')

# essential spices 
only_in_essential = essential_spices - optional_spices
print(f'Only essential Spices: {only_in_essential}')

# membership test 
print(f"Is 'cloves' in essential spices? {'cloves' in essential_spices} ")

# optional spices
print(f"Is 'cloves' in optional spices? {'cloves' in essential_spices} ")

