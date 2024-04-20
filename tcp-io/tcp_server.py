

# luis arandas 02-04-2024
# Simple server to illustrate TCP io between TouchDesigner session and CMD

import socket
import random

# ! Should start before tcp.toe

class TCPServer:
	def __init__(self, ip='127.0.0.1', port=7001, buffer_size=512):
		self.ip = ip
		self.port = port
		self.buffer_size = buffer_size
		self.socket = None
		self.conn = None
		self.addr = None
		self.is_listening = True  # Control listening state

	def start_server(self):
		# Starts the TCP server and accepts a connection
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.bind((self.ip, self.port))
		self.socket.listen(1)
		print(f"Server started on {self.ip}:{self.port}. Waiting for connection...")
		self.conn, self.addr = self.socket.accept()
		print(f"Connection established with: {self.addr}")

	def listen_once(self):
		# Listens for a single message and processes it
		if self.conn:
			data = self.conn.recv(self.buffer_size)
			if data:
				decoded_data = data.decode('utf-8')
				print('Message received:', decoded_data)
				self.process_data(decoded_data)
			else:
				print("No data received. Possible disconnection.")
				self.is_listening = False

	def listen_loop(self):
		# Keeps listening for messages until is_listening is False
		while self.is_listening and self.conn:
			try:
				self.listen_once()
			except ConnectionResetError:
				print("Connection was reset. Closing connection.")
				break

	def process_data(self, data):
		# Process the received data
		if 'Message' in data:
			random_int = random.randint(1, 100)
			response = f'Return from the Server! Random val: {random_int}'
			self.conn.send(response.encode('utf-8'))
		elif 'quit' in data:
			print("Quit command received. Stopping server.")
			self.is_listening = False


	def close_connection(self):
		# Closes the current connection and server socket
		if self.conn:
			self.conn.close()
			self.conn = None
			print("Connection closed.")
		if self.socket:
			self.socket.close()
			print("Server socket closed.")


if __name__ == "__main__":
    server = TCPServer()
    server.start_server()
    # Use server.listen_once() if you want to handle a single message
    # or server.listen_loop() to continuously listen for messages.
    server.listen_loop()  # Continuously listen until 'quit' command is received
    server.close_connection()
    
