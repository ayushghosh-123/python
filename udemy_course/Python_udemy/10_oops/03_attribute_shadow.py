class Chai:
    temperature = 'hot'
    strength = 'Strong'

cutting = Chai()
print(cutting.temperature)

cutting.temperature = 'Mild'
cutting.cup = 'Small'

print('After changing', cutting.temperature)
print('direct look into the class', Chai.temperature)
print('cup size is: ', cutting.cup)



del cutting.temperature
print(cutting.temperature)
print(cutting.cup)