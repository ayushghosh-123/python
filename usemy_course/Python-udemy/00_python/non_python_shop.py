class Chai:
    def __init__(self , sweetness, milk_level): # intialize the class 
        self.sweetness = sweetness
        self.milk_level = milk_level
    
    def sip(self):
        print("sipping chai")

    def add_sugar(self, amout):
        print("added the sugar")

# object of class Chai
my_chai = Chai(sweetness=3, milk_level=2)
my_chai.add_sugar(3)