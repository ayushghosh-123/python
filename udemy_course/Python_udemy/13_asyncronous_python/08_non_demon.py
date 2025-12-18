import threading
import time

def monitor_tea_temp():
    while True:
        print("Monitoring tea temperature...")
        time.sleep(2)

# Create and start the thread
t = threading.Thread(target=monitor_tea_temp)
t.daemon = True  # ✅ ensures the thread stops when the main program exits
t.start()

print("Main program done...")
