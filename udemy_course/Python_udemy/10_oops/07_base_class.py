class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


# def GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#             self.type= type_
#             self.strenth = strength
#             self.spice_level = spice_level

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level

class GingerChai(Chai):
    def __init__(self, type_, strength):
        super().__init__(type_, strength)