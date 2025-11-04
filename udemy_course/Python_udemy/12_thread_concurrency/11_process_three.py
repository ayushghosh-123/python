from multiprocessing import Process, Queue, Value

def prepare_chai(queue):
    queue.put("Masala chai ready")

Counter = Value('i', 0)

queue = Queue()

p = Process(target=prepare_chai, args=(queue,))
p.start()
p.join()
print(queue.get())
