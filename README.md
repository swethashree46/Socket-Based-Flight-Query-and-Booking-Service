
# Flight Booking and Query System

## Overview

This project is a simulation of a flight booking system, where users can interact with a server via a client application. The system allows users to query available countries, book flights between those countries, and check the status of their booking (whether the ticket is booked or pending).

The system is implemented using **Python's socket programming** for communication between the server and client. The server listens for client requests and responds with flight details, booking status, or error messages.

## Features

- **Country Query**: Users can input country names (USA, India, UK) to receive a welcome message.
- **Flight Booking**: Users can input flight details (source, destination, date, and time) for booking.
- **Booking Status**: After submitting flight details, users are informed whether the booking was successful or still pending.
- **Stop Command**: Users can stop the connection by sending the "STOP" command.

## Components

1. **Server (server.py)**:
   - Listens for incoming client connections.
   - Handles queries, flight bookings, and sends responses.
   - Simulates flight booking status (booked or pending).
   
2. **Client (client.py)**:
   - Connects to the server.
   - Allows users to input queries or flight details.
   - Displays the booking status or other relevant messages received from the server.

## Setup Instructions

### Prerequisites

- Python 3.x installed on your machine.
- Basic understanding of socket programming.

### Running the Server

1. Save the server code in a file named `server.py`.
2. Open a terminal and navigate to the directory containing `server.py`.
3. Run the server with the following command:

   ```bash
   python server.py
   ```

   The server will start listening for incoming client connections on `127.0.0.1` (localhost) and port `9999`.

### Running the Client

1. Save the client code in a file named `client.py`.
2. Open a new terminal and navigate to the directory containing `client.py`.
3. Run the client with the following command:

   ```bash
   python client.py
   ```

4. The client will prompt you to enter a query, such as a country name (`USA`, `IND`, `UK`), the word `flight` to book a flight, or `STOP` to end the session.

### Sample Interaction

- **Client**: `USA`
  - **Server**: `Welcome to USA`
  
- **Client**: `flight`
  - **Server**: `Please enter the source country, destination country, and travel date/time (format: source,destination,date,time):`
  
- **Client**: `USA,IND,2024-12-15,10:00`
  - **Server**: `Booking flight from USA to IND on 2024-12-15 at 10:00. Status: Booked`

- **Client**: `STOP`
  - **Server**: `STOPPED`

## Customization

- You can modify the list of valid countries by changing the `valid_countries` list in the server code.
- The flight booking status is simulated with a fixed value (`booked` or `pending`), but you can expand this logic to incorporate a more complex booking system or database integration.

## License

This project is open source and available under the [MIT License](LICENSE).
```

