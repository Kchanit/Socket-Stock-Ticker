# Stock Ticker

This project implements a simple stock ticker server using socket programming. It allows clients to connect and retrieve real-time stock prices using the Yahoo Finance API.

## Prerequisites

- Python 3.x
- `yfinance` library (install using `pip3 install yfinance`)

## Usage

### Server

```bash
python3 server.py
```

The server will start listening for connections on port 9999.

### Client

```
python3 client.py
```

The client can enter commands to retrieve stock prices or exit the program.

### Command Format

- To retrieve a stock price: `GET <stock symbol>`
  Example: `GET MSFT`
- To retrieve prices for multiple stocks: `GET <stock symbol 1>,<stock symbol 2>,...`
  Example: `GET AAPL,MSFT,GOOG`
- To exit the program: `EXIT`

### Note

- The server must be running before clients can connect.
- Ensure the yfinance library is installed.

Feel free to explore and enhance the functionality as needed.
