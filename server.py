import socket

# Create a socket object
print("I am server. I am starting a new stream for any queries:")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host and port settings
host = '127.0.0.1'
port = 9999

# Bind to the port and listen
serversocket.bind((host, port))
serversocket.listen(5)

# Accept a client connection
clientsocket, addr = serversocket.accept()
print("=======> ", clientsocket, addr)
print("Got a connection from %s" % str(addr))

while True:
    q = clientsocket.recv(2048)
    print(" ***************> ", q, type(q))
    qs = q.decode('ascii')
    print("========> ", qs, type(qs))

    if qs in ['USA', 'IND', 'UK']:
        msg = "Welcome to " + str(qs)
        clientsocket.send(msg.encode('ascii'))

    elif qs == "flight":
        # Ask for source and destination countries
        msg = "Please enter the source country, destination country, and travel date/time (format: source,destination,date,time):"
        clientsocket.send(msg.encode('ascii'))
        # Receive the flight details from the client
        flight_details = clientsocket.recv(2048).decode('ascii')
        try:
            source, destination, travel_date, travel_time = flight_details.split(',')

            # Validate countries and timings
            valid_countries = ['USA', 'IND', 'UK']
            if source in valid_countries and destination in valid_countries:
                # Simulate booking status (can be pending or booked)
                booking_status = "booked"  # Set to "pending" if needed
                msg = f"Booking flight from {source} to {destination} on {travel_date} at {travel_time}. Status: {booking_status.capitalize()}"
            else:
                msg = "Invalid countries. Please use valid options: USA, IND, UK."
        except ValueError:
            msg = "Invalid format. Please provide input as: source,destination,date,time."

        clientsocket.send(msg.encode('ascii'))

    elif qs == "STOP":
        msg = "STOPPED"
        clientsocket.send(msg.encode('ascii'))
        break

    else:
        msg = "Not supporting the country " + qs
        clientsocket.send(msg.encode('ascii'))

clientsocket.close()
print("Ended here")
