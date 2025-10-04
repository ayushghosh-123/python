chai_type = "pLain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = 'Irnai'
    kitchen()

front_desk()
print("Final Global Chai: ", chai_type)
