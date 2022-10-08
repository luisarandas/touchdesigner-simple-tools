

# luis arandas 19-09-2022
# simple server, careful to scale this as object

import socket

# set server variables
TCP_IP = '127.0.0.1'
TCP_PORT = 7001
BUFFER_SIZE  = 512 # 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()

# print connection address when someone connects
print('Connection address:', conn, addr)

# start main loop
while 1:
	# listen for calls
	data = conn.recv(BUFFER_SIZE)
	data = data.decode('utf-8')
	print('message received:: ', data)
	# if someone calls with hello, respond
	if 'hello' in data:
		delivery = 'Hello from Python!!'
		conn.send(delivery.encode('utf-8'))

conn.close()