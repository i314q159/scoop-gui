import os
import time

t1 = time.time()
os.system("scoop import scoop.json")
t2 = time.time()
print(f"{(t2 - t1) * 1000:.2f} ms")
