# dictionary 
chai_order = dict(type='Masala Chai', size ='Large', sugar=2)
print(f'Chai Order : {chai_order}')

chai_recepie = {}
chai_recepie["base"] = "black tea"
chai_recepie["liquid"] = "milk"
print(f'Recipe base: {chai_recepie['base']}')


del chai_recepie['liquid']
print(f"Recipe: {chai_recepie}")

print(f'Is sugar in the order? {'sugar' in chai_order}')


# print(f'order details (keys): {chai_order.keys()}')
# print(f'order details (keys): {chai_order.values()}')
# print(f'order details (keys): {chai_order.items()}')



chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}
last_item = chai_order.popitem()
print(f'Remove last item: {last_item}')

extra_spices = {"cardmom": "crunched", "ginger": "sliced"}
chai_recepie.update(extra_spices)
print(f'Update chai recipe: {chai_recepie}')


# Chai_size = chai_order['Customer_note']
Chai_size = chai_order.get('note', "NO Note")
print(f'Chai size is: {Chai_size}')



