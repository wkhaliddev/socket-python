import socket
#import sys
import zipfile as zip
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('[+] Client socket is created.')

s.connect((socket.gethostname(),50000))
print('[+] Socket is connected to localhost with port 50000')
filename='rana2.zip'
f = open(filename, 'wb')
reciever_writer = s.recv(1024)
while(reciever_writer):
	f.write(reciever_writer)
	reciever_writer = s.recv(1024)
f.close()
print('[+] Received file ' + filename)

with zip.ZipFile(filename, 'r') as file:
	print('[+] Extracting files...')
	file.extractall()
	print('[+] Done')

os.remove(filename)
f.close()
s.close()
