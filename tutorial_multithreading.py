import time
import threading

def foo(arg):
    print("Going in")
    time.sleep(arg)
    print("Coming out")

start_time = time.time()
foo(2)
foo(2)
end_time = time.time()
print("total time", end_time - start_time)

"""
Results:
Going in
Coming out
Going in
Coming out
total time 4.004383325576782
"""
# these are io bound work so can be threaded

t1 = threading.Thread(target=foo, args=[2]) # target=foo, args, kwargs
t2 = threading.Thread(target=foo, args=[2])

start_time = time.time()
t1.start()
t2.start()

t1.join()
t2.join()
end_time = time.time()
print("total time", end_time - start_time)

"""
Results:
Going in
Going in
Coming out
Coming out
total time 2.0041699409484863
"""