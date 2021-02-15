import socket as sck
import hashlib
import time as tm

start = tm.time()
f = open("p1.txt")
#ip = sck.gethostbyname('vayu.iitd.ac.in')
#print("IP: ", ip, "\n")

serverPort = 80
clientSocket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
clientSocket.connect(('norvig.com', serverPort))
sentence = f.read()
print("HTTP Request Header\n")
print(sentence)
clientSocket.send(sentence.encode())
file = ''

while True:
    modifiedSentence = clientSocket.recv(1)
    data = modifiedSentence.decode()
    if len(data) == 0:
        break
    file += data

pos = file.find("\r\n\r\n")
file = file[pos+4:]
#print(file)
try:
    x = file.find("<!DOCTYPE html>")
    if x != -1:
        file = file[:x]
except:
    pass

f1 = open("data1.txt", "w")
f1.write(file)
f1.close()

original_md5 = "70a4b9f4707d258f559f91615297a3ec"

md = hashlib.md5(file.encode())
print(md.hexdigest())

if md.hexdigest() == original_md5:
    print("Hash matched: ", md.hexdigest())
else:
    print("Hash don't match: ", md.hexdigest())

end = tm.time()
print("\nDone!!")
print("Time Take: ", end-start)

#70a4b9f4707d258f559f91615297a3ec
#70a4b9f4707d258f559f91615297a3ec
#70a4b9f4707d258f559f91615297a3ec
#((ip.src==192.168.43.42 && ip.dst==158.106.138.13) || (ip.src==158.106.138.13 && ip.dst==192.168.43.42)) && http