def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"
    yield "Lemon Chai"

def imported_chai():
    yield "Green Tea"
    yield "Oolong Tea"
    yield "Chamomile Tea"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order..."
            print(f"Preparing {order}")
    except GeneratorExit:
        print("Stall closed, no more chai.")

stall = chai_stall()
print(next(stall))  # Starts the generator
stall.send("Masala Chai")  # Sends an order
stall.close()  # Closes the stall

    