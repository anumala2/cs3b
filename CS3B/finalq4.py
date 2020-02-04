
"""

from tkinter import Tk, Label, PhotoImage, TOP, LEFT, RIGHT

root = Tk()

text = Label(root, 
             font=('Helvetica', 16, 'bold italic'), 
             foreground='white', 
             background='black', 
             padx=25, 
             pady=10, 
             text='Dogs WOOF!, cats MEOW!')
text.pack(side=TOP) 

dog = PhotoImage(file='dog.gif')
dogLabel = Label(root,
                 borderwidth=3,
                 image=dog)
dogLabel.pack(side=LEFT) 

cat = PhotoImage(file='cat.gif')
catLabel = Label(root,
                 image=cat)
catLabel.pack(side=RIGHT) 

root.mainloop()


from tkinter import Tk, Label, PhotoImage, BOTTOM, LEFT, RIGHT

root = Tk()

text = Label(root, 
             font=('Helvetica', 16, 'bold italic'), 
             foreground='white', 
             background='black', 
             padx=25, 
             pady=10, 
             text='Dogs WOOF!, cats MEOW!')
text.pack(side=BOTTOM) 

dog = PhotoImage(file='cat.gif')
dogLabel = Label(root,
                 borderwidth=3,
                 image=dog)
dogLabel.pack(side=LEFT) 

cat = PhotoImage(file='dog.gif')
catLabel = Label(root,
                 image=cat)
catLabel.pack(side=RIGHT) 

root.mainloop()


from tkinter import Tk, Label, PhotoImage, BOTTOM, LEFT, RIGHT

root = Tk()

text = Label(root, 
             font=('Helvetica', 16, 'bold italic'), 
             foreground='white', 
             background='black', 
             padx=25, 
             pady=10, 
             text='Dogs WOOF!, cats MEOW!')
text.pack(side=BOTTOM) 

dog = PhotoImage(file='dog.gif')
dogLabel = Label(root,
                 borderwidth=3,
                 image=dog)
dogLabel.pack(side=LEFT) 

cat = PhotoImage(file='cat.gif')
catLabel = Label(root,
                 image=cat)
catLabel.pack(side=RIGHT) 

root.mainloop()


import threading
from time import sleep, ctime

loops =[4,2]

def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'doneat:', ctime())

def main():
    print('starting at:' , ctime())
    threads = []

    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,
        args = (i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    tst = threading.enumerate()
    print("\n\n\n", "TST ONE:", tst)

    for i in nloops:
        threads[i].join()

    print('all DONE at:', ctime())

    tst2 = threading.enumerate()
    print("\n\n\n", "TST TWO:", tst2)

if __name__ =='__main__':
 main()


from tkinter import Tk, Label, PhotoImage, TOP, LEFT, RIGHT
root = Tk()

label = Label(root, text="Foothill College")
label.grid(row=0, column=1)
root.mainloop()

import socket

HOST = socket.gethostname()
PORT = 50007 # Arbitrary non-privileged port used

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
        print("dead")
    conn.send(data)
    print("not dead")
conn.close()
print("finish")


from wsgiref.simple_server import make_server

def hello_app(environ, start_response):
    start_response("200 OK", [("Content-type", "text/plain")])
    return["Hello Foothill!".encode("utf-8")]

server = make_server('localhost', 2156, hello_app)

server.serve_forever()


from tkinter import Tk, Label, PhotoImage, TOP, LEFT, RIGHT
root = Tk()
widget = Label(root, text='Hello Foothill!')
widget.pack(side=RIGHT)
widget.mainloop()


import urllib.request                  
url = 'http://www.nytimes.com'

request = urllib.request.urlopen(url)
text = request.read()
text = text.decode('utf-8')             # Option a

import urllib.request
url = 'http://www.nytimes.com'

request = urllib.request.urlopen(url)
text = request.read()
text = text.decode('latin-1')           # Option b

def test_one(old_func):
    def new_func(*args, **kwargs):
        return old_func(*args, **kwargs) + 1
    return new_func

@test_one
def sum_two(val1, val2):
    return val1 + val2

result = sum_two(5,7)
print(result)



def add(num1, num2):
    result = num1 + num2 
    print(result)           # line 1

add(1,2)
print(result)               # line 2


import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 6532))
s.listen()
print("l")
a, b = s.accept()
print(a)
print(b)
print("done")

import sqlite3

con = sqlite3.connect(":memory:")
con.isolation_level = None
cur = con.cursor()

fmidList = [1234, 1235, 1236]
marketList = ["Corn", "Cotton", "Hay"]
profitList = [36, 45, 45]
cur.execute('CREATE TABLE IF NOT EXISTS fmarket ( fmid INTEGER, \
             market TEXT, profit INT)')
for i in range(len(fmidList)):
    cur.execute('INSERT INTO fmarket VALUES (?, ?, ?)',
                (fmidList[i], marketList[i], profitList[i]))
con.commit()


import re
matcher = re.compile(r"ab*")
match_list = list(matcher.finditer("cdabbabc"))
print(match_list)
for m in match_list:
    print(m.start(), m.end())


import time
from threading import Thread
sleepTime = 1

def countdown(n):
    while n > 0:
        print('Time remaining: ', n)
        n -=1
        time.sleep(sleepTime)

aThread = Thread(target=countdown, args=(10,))
aThread.start()

"""
from collections import OrderedDict

fruit = OrderedDict([("banana", 2), ("apple", 1), ("orange", 3)])
for key, value in fruit.items():
    print(key, value)
