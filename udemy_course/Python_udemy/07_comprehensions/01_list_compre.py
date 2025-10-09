menu = [
    "Masala chai",
    "Iced Lemon Tea",
    "Grean Tea",
    "Iced Peach Tea",
    "Ginger Chai"
]

iced_tea = [my_tea for my_tea in menu if len(my_tea) > 10]
print(iced_tea)