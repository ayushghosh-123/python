# Tuple
masala_spices = ("cardamon", "cloves", "cinnamon")


# destructuring by this way 
(spice1, spice2, spice3) = masala_spices
print(f"Main masala spices: {spice1}, {spice2}, {spice3}")


ginger_ratio, cadraMon_ratio = 2, 1
print(f"Ratio is G : {ginger_ratio} and C: {cadraMon_ratio}")

ginger_ratio , cadraMon_ratio = cadraMon_ratio, ginger_ratio
print(f"Ratio is G : {ginger_ratio} and C: {cadraMon_ratio}")


#membership testing 

# in -> a big role in tuple 
print(f"Is ginger in masala spices ? {'ginger' in masala_spices}")
print(f"Is ginger in masala spices ? {'cinnamon' in masala_spices}")

 