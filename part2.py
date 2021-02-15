import socket as sck
import hashlib

f = open("p2.txt")
ip = sck.gethostbyname('norvig.com')
print("IP: ", ip, "\n")

serverPort = 80
clientSocket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
clientSocket.connect(('norvig.com', serverPort))
sentence = f.read()
print("HTTP Request Header\n")
print(sentence)
clientSocket.send(sentence.encode())
file = ''

while True:
    modifiedSentence = clientSocket.recv(1024)
    data = modifiedSentence.decode()
    if len(data) == 0:
        break
    file += data

pos = file.find("\r\n\r\n")
file = file[pos+4:]

f1 = open("data2.txt", "w")
f1.write(file)
f1.close()
