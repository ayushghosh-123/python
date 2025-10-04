chai_type='ginger'

def updated_order():
    chai_type = 'Elaichi'
    def kitchen():
        nonlocal chai_type 
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update: ", chai_type)

updated_order()