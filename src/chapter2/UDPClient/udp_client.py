import socket

target_host = '127.0.0.1'
target_port = 80

# Create a UDP socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Notice we skip the connect step here when compared to TCP
# because UDP is a connectionless protocol

# Send some data
client.sendto(b"ABCDEFG", (target_host, target_port))

# Receive some data
data = client.recvfrom(4096)
print(data)
