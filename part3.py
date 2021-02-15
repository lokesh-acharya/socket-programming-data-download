from os import name
import socket as sck
import math
import hashlib
import time
import threading as thr
from _thread import *

class tcp_thread(thr.Thread):
    def __init__(self, dataReq, i):
        super(tcp_thread, self).__init__()
        self.strt = dataReq+0
        self.num = i
        self.val = dataReq + THREAD_LIFE*BLOCK_SIZE
        self.soc = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    
    def value(self):
        return self.val

    def run(self):
        self.soc.connect(('norvig.com', 80))
        for i in range(THREAD_LIFE):
            self.soc.sendall((tmp +str(self.strt+i*BLOCK_SIZE)+"-"+str(self.strt+(i+1)*BLOCK_SIZE-1)+"\r\n\r\n").encode())
        dataChunk = ''
        while True:
            modifiedSentence = self.soc.recv(1024)
            data = modifiedSentence.decode()
            if len(data) == 0:
                break
            dataChunk += data
        fileData.append((self.num, dataChunk))

start_time = time.time()

n = int(input("number of connections: "))
SIZE = 6488666
BLOCK_SIZE = 10000
THREAD_LIFE = math.ceil(SIZE/(BLOCK_SIZE*n))
#n = math.ceil(SIZE/(BLOCK_SIZE*THREAD_LIFE))
tmp = "GET /big.txt HTTP/1.1\r\nHost: norvig.com\r\nConnection: keep-alive\r\nRange: bytes="

fileData = []
thread_list = []
dataReq = 0

for i in range(n):
    print("creating new tcp thread")
    t = tcp_thread(dataReq, i)
    dataReq = t.value()
    thread_list.append(t)
    print(dataReq)

for t in thread_list:
    print("starting the thread")
    t.start()

for t in thread_list:
    t.join()
    print("+++++++++++++++++++++++ Thread joined ++++++++++++++++++")

end_time = time.time()
print("\nDone!!")
print("Execution Time: ", end_time-start_time)

fileData = sorted(fileData, key=lambda x: x[0])
#fileData.reverse()

file = ''
for s in fileData:
    print(s[0])
    file += s[1]

while True:
    x = file.find("HTTP/1.1")
    if x == -1:
        break
    else:
        y = file.find("\r\n\r\n")
        if y != -1:
            file = file[:x] + file[y+4:]
try:
    x = file.find("<!DOCTYPE html>")
    if x != -1:
        file = file[:x]
except:
    pass

f = open("part3data.txt", "w")
f.write(file)
f.close()

original_md5 = "70a4b9f4707d258f559f91615297a3ec"

md = hashlib.md5(file.encode())
print(md.hexdigest())

end_time = time.time()
print("\nDone!!")
print("Execution Time: ", end_time-start_time)
