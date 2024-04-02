# test_udp.py

import socket
import random  # Import the random module

def send_data_to_touchdesigner(data, ip='127.0.0.1', port=7000):
    # Generate a random integer between a specified range, e.g., 0 to 999
    random_int = random.randint(0, 999)
    # Append the random integer to the data string
    data_with_random = f"{data} {random_int}"
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto(data_with_random.encode(), (ip, port))

if __name__ == "__main__":
    send_data_to_touchdesigner("Hello TouchDesigner")
    print("ran: 'send_data_to_touchdesigner()'")