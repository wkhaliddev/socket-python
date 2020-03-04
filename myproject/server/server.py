import socket
#import sys
import zipfile as zip
import os


zip_name = 'rana.zip'

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(' Server socket is created.')
ss.bind((socket.gethostname(),50000))
print(' Socket is connected to localhost with port 50000')

ss.listen(5)
print(' Waiting for connection...')

con, addr = ss.accept()
#print("port is :",addr)
print(' Got connection from {}{}'.format(addr[0],addr[1]))

with zip.ZipFile(zip_name, 'w') as file:
	file.write('{}.jpg'.format(1))
	print('[+] {}.jpg is sent'.format(1))

f = open(zip_name, 'rb')
reader_sender = f.read()
print("agya",reader_sender)
con.sendall(reader_sender)

f.close()
ss.close()
os.remove(zip_name)
