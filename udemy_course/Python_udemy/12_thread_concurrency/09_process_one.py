import threading
import time

def cpu_heavy():
    print(f'crunching some numbers...')
    total = 0
    for i in range(10**7):
        total +=i
    print("Done ")

start = time.time()