import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
	connection, address = s.accept()
	child_pid = os.fork()
	while True:
		data = connection.recv(1024)
		if not data or data == 'close':
			break
		connection.send(data)
	connection.close()
