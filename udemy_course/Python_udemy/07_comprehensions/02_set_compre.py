# favourite_chais = ["Masal Chai", "Green Tea", "Masala Chai", "Lemon Tea", "Green Tea", "Elachi Chai"]

# unique_chai = {chai for chai in favourite_chais if len(chai) <8} 
# print(unique_chai)

recepie = {
    "Masala Chai" : ['ginger', 'cardamom', 'clove'],
    "Elaichi Chai" : ['cardamon', 'milk'],
    "Spicy Chai" : ['ginger', 'black pepper', 'clove']
}

unique_spices = {spice for ingredients in recepie.values() for spice in ingredients}

print(unique_spices)  