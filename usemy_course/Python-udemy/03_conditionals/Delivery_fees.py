order_amount = int(input("Enter the order amount: "))

# ternary operator
delivery_fees = 0 if order_amount > 300 else 30 # agar order_amount 300 jsai jada hoga to delivery_fees 0 na to 30

print(f'Delivery fees is: {delivery_fees}')


