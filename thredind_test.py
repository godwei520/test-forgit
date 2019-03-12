import threading
import time


def run(n):
    print(n)

for i in range(10):
    t = threading.Thread(target=run, args=(i,))
    t.start()

