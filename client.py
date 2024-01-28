import socket
import threading


def send_message(client, message):
    client.send(message.encode())


def receive_data(client):
    try:
        data = client.recv(1024).decode()
        print(data)
    except Exception as e:
        print(f"Error receiving data: {e}")


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(("localhost", 9999))
        print("Connected to the Stock Ticker Server.")
    except Exception as e:
        print(f"Error connecting to the server: {e}")
        return

    try:
        while True:
            message = input(
                "Enter command (GET <stock symbol>, exit): ")

            if message.lower() == "exit":
                print("Exiting the client...")
                send_message(client, message)
                client.close()
                break

            # Start the send_thread when the user enters a command
            send_thread = threading.Thread(
                target=send_message, args=(client, message))
            send_thread.start()
            # Start the receive_data thread immediately after connecting
            receive_thread = threading.Thread(
                target=receive_data, args=(client,))
            receive_thread.start()

            # Wait for both threads to finish before starting the next iteration
            send_thread.join()
            receive_thread.join()

    except Exception as e:
        print(f"Error in client: {e}")

    client.close()


if __name__ == "__main__":
    start_client()
