import threading
import time

def brew_chai():
    print(f'{threading.current_thread().name} started brewing')
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f'{threading.current_thread().name} finished brewing')

# Create threads
thread1 = threading.Thread(target=brew_chai, name='Barista-1')
thread2 = threading.Thread(target=brew_chai, name='Barista-2')

# Start timing
start = time.time()

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# End timing
end = time.time()

print(f'Total time taken: {end - start:.2f} seconds')
