# String
chai_type = "Ginger Chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} pleease !")

# indexing and slicing
chai_description = "Aromatic and Bold"
print(f"First word : {chai_description[0:7]}")
print(f"First word : {chai_description[0:8:2]}")
print(f"First word : {chai_description[12:]}")
print(f"First word : {chai_description[:-1]}")

label_text = "chai Special"
encoded_lebel = label_text.encode("utf-8")
print(f"No n label: {label_text}")
print(f"Encoded label: {encoded_lebel}")
decoded_lebel = encoded_lebel.decode('utf-8')
print(f"Decoded label: {decoded_lebel}")

