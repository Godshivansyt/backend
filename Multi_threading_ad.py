import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

# craete a thread 
t = threading.Thread(target= print_numbers)

# start the thread 
t.start()

# main thread continues to run in parallel
for i in range(5):
     print(f"Main Thread: {i}")
     time.sleep(1)
    
    # wait for the thread to finish 
t.join()
print("Thread Completed.") 


#  Synchronizing Threads

#  lock example

lock = threading.Lock()
def print_safe_numbers():
    with lock:
        for i in range(5):
            print(f"Safe Number: {i}")
            time.sleep(1)

thread1 = threading.Thread(target=print_safe_numbers)
thread2 = threading.Thread(target=print_safe_numbers)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

            
            
 # . Thread Communication Using Queue
import queue

q = queue.Queue()

def producer():
    for i in range(5):
        q.put(i)
        print(f"Producer: {i}")
    
    
def consumer():
    while not q.empty():
        item = q.get()
        print(f"Consumed : {item}")  
        q.task_done()      
     
# create threads 
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

# start threads
t1.start()
t2.start()        

# wait for threads to complete
t1.join()
t2.join()


import threading
import time

def meeting():
    print("Meeting Started")
    for i in range(5):
        print(f"Person: {i} JOined this meeting.")
        time.sleep(2)

t = threading.Thread(target=meeting)

t.start()

for i in range(5):
    print(f"Employee: {i} joined this meeting.") 
    time.sleep(1)
    
t.join()           
print("Thread Completed.")  
      
    