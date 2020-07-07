import socket

target_host = "google.com"
target_port = 8080

# Create a TCP socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to target
client.connect((target_host, target_port))

# Send some data
client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

# Receive some data
response = client.recv(4096)
print(response)
