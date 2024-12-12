import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host and port settings
host = '127.0.0.1'
port = 9999
print(host)

# Connect to the server
s.connect((host, port))

while True:
    i = input("Enter your query (e.g., country name or 'flight' or 'STOP'): ")
    s.send(i.encode('ascii'))

    msg = s.recv(1024)
    print("========> ", msg.decode('ascii'))
    msg_str = msg.decode('ascii')

    if "source country" in msg_str:
        flight_details = input("Provide source, destination, date, and time (format: source,destination,date,time): ")
        s.send(flight_details.encode('ascii'))
        msg = s.recv(1024)
        print("========> ", msg.decode('ascii'))

    if msg_str == "STOPPED":
        break

s.close()
