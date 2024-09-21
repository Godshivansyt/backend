import multiprocessing
import time

def print_numbers():
    for i in range(5):
        print(f"Process Number: {i}")
        time.sleep(1)
 
if __name__ == "__main__":
    p = multiprocessing.Process(target=print_numbers)         
    p.start()
    
    for i in range(5):
        print(f"Main Process: {i}")
        time.sleep(1)
        
    p.join()
    print("Process Completed!.")        
    

def producer(queue):
    for i in range(5):
        queue.put(i)
        print(f"Produced {i}")

def consumer(queue):
    while not queue.empty():
        item = queue.get()
        print(f"Consumed {item}")

if __name__ == "__main__":
    q = multiprocessing.Queue()
    
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    