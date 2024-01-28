import socket
import threading
import yfinance as yf
import time


def get_stock_price(symbol):
    res = yf.Ticker(symbol)
    if res.info['quoteType'] == "NONE":
        return "Invalid symbol"
    else:
        price = '$'+str(res.info['currentPrice'])
        return price


def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode().upper()

            if data.startswith("GET"):
                symbol = data.split()[1]
                response = get_stock_price(symbol)
                response = f"{symbol}: {response}"
                client_socket.send(response.encode())

            elif data == "EXIT":
                goodbye_message = "Goodbye!"
                client_socket.send(goodbye_message.encode())
                client_socket.close()
                break

            else:
                error_message = "ERROR: Invalid command\n"
                client_socket.send(error_message.encode())

        except Exception as e:
            print(f"Error handling client: {e}")
            break


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("Stock Ticker Server is listening for connections...")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")

        # welcome_message = "Welcome to Stock Ticker Server\n"
        # client_socket.send(welcome_message.encode())

        client_handler = threading.Thread(
            target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    start_server()
