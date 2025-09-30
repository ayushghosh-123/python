# value = 13
# remainder = value % 5
# if remainder:
#     print(f'Not divisible, remainder is: {remainder}')



#warlus opertor
value = 13
if (remainder := value % 5):
    print(f'Not divisible, remainder is: {remainder}')

available_sizes = ['small', 'medium', 'large']
if(requested_size := input("Enter your chai cup size :")) in available_sizes:
    print(f'Serving {requested_size} chai')
else:
    print(f'size is unavaible - {requested_size}')

flavours = ['masala', 'ginger', 'lemon', 'mint']
print('Available flavours: ', flavours)

while (flavours := input('choose your flavor: '))not in flavours:
    print(f'sorry, {flavours} is not available')

print(f'you choose {flavours} chai')