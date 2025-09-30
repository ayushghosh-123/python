flavours = ["ginger", "Out of stock", "Lemon", "DisContinued", "Tulsi"]

for flavour in flavours:
     if flavour == 'Out of stock':
          continue
     if flavour == "Discontinued":
          print(f'{flavour} item found')
          break
     print("discount item is found")

print("Out of this")