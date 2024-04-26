import websocket

# Set the WebSocket endpoint URL
url = "ws://localhost:8001/ws"

# Create a WebSocket connection
ws = websocket.create_connection(url)

# Send a message to the server
ws.send("Hello, server!")

# Receive a response from the server
response = ws.recv()
print(f"Received: {response}")

# Close the WebSocket connection
ws.close()