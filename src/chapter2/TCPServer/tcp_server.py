import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 8080


# Client handling thread
def handle_client(client_socket):
    # Receive some data
    request = client_socket.recv(1024)
    print(f"[*] Received: {request}")

    # Send some data
    client_socket.send(b"ACK!")

    # Close the connection
    client_socket.close()


# Create TCP socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set server binding address
server.bind((bind_ip, bind_port))

# Begin listening, allowing up to 5 backlogged connections
server.listen(5)
print(f"[*] Listening on {bind_ip}:{bind_port}")

# Main loop
while True:
    # Wait for a connection
    client, addr = server.accept()
    print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")

    # Start thread to handle request
    client_thread = threading.Thread(target=handle_client, args=(client,))
    client_thread.start()
