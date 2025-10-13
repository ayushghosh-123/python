# def serve_chai():
#     yield "Cup 1: Masala Chai"
#     yield "Cup 2: Ginger Chai"
#     yield "Cup 3: Elachi Chai"

# stall = serve_chai()
# for cup in stall:
#     print(cup)

def get_chai_list():
    return['cup 1', 'cup 2', 'cup 3']

#generate function

def get_chai_get():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_get()
print(next(chai))
print(next(chai))
print(next(chai))
# print(next(chai)) gives error