# DES Encryption/Decryption HTTP Server & Client

A DES (Data Encryption Standard) implementation with HTTP-based client-server architecture, compatible with localtunnel for remote access.

## Features

- HTTP-based communication (compatible with localtunnel)
- RESTful API endpoints for encryption and decryption
- Interactive command-line client
- Support for both local and remote connections
- CORS enabled for web access

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Starting the Server

Run the server locally:
```bash
python des_server.py
```

The server will start on `http://0.0.0.0:5000`.

### Using Localtunnel

To expose your local server to the internet using localtunnel:

1. Install localtunnel (requires Node.js):
```bash
npm install -g localtunnel
```

2. Start your DES server:
```bash
python des_server.py
```

3. In a new terminal, start localtunnel:
```bash
lt --port 5000
```

4. Localtunnel will provide a public URL (e.g., `https://your-tunnel.loca.lt`)

5. Use this URL in the client to connect remotely!

### Using the Client

Run the client:
```bash
python des_client.py
```

When prompted:
- For local connection: Enter `http://localhost` or `http://127.0.0.1`
- For localtunnel connection: Enter the URL provided by localtunnel (e.g., `https://your-tunnel.loca.lt`)

## API Endpoints

### GET /
Returns server information and available endpoints.

**Response:**
```json
{
  "status": "success",
  "message": "DES Encryption/Decryption Server is running",
  "endpoints": {
    "/": "GET - Server info",
    "/encrypt": "POST - Encrypt data",
    "/decrypt": "POST - Decrypt data",
    "/process": "POST - Encrypt or decrypt based on operation parameter"
  }
}
```

### POST /process
Encrypt or decrypt data based on the operation parameter.

**Request:**
```json
{
  "operation": "ENCRYPT",  // or "DECRYPT"
  "plaintext": "0123456789ABCDEF",
  "key": "133457799BBCDFF1"
}
```

**Response (Encrypt):**
```json
{
  "status": "success",
  "operation": "encrypt",
  "plaintext": "0123456789ABCDEF",
  "key": "133457799BBCDFF1",
  "ciphertext": "85E813540F0AB405"
}
```

### POST /encrypt
Encrypt plaintext.

**Request:**
```json
{
  "plaintext": "0123456789ABCDEF",
  "key": "133457799BBCDFF1"
}
```

**Response:**
```json
{
  "status": "success",
  "operation": "encrypt",
  "plaintext": "0123456789ABCDEF",
  "key": "133457799BBCDFF1",
  "ciphertext": "85E813540F0AB405"
}
```

### POST /decrypt
Decrypt ciphertext.

**Request:**
```json
{
  "ciphertext": "85E813540F0AB405",
  "key": "133457799BBCDFF1"
}
```

**Response:**
```json
{
  "status": "success",
  "operation": "decrypt",
  "ciphertext": "85E813540F0AB405",
  "key": "133457799BBCDFF1",
  "plaintext": "0123456789ABCDEF"
}
```

## Testing with cURL

### Test server connection:
```bash
curl http://localhost/
```

### Encrypt data:
```bash
curl -X POST http://localhost/encrypt \
  -H "Content-Type: application/json" \
  -d '{"plaintext": "0123456789ABCDEF", "key": "133457799BBCDFF1"}'
```

### Decrypt data:
```bash
curl -X POST http://localhost/decrypt \
  -H "Content-Type: application/json" \
  -d '{"ciphertext": "85E813540F0AB405", "key": "133457799BBCDFF1"}'
```

## Input Format

- **Plaintext/Ciphertext**: Exactly 16 hexadecimal characters (64 bits)
- **Key**: Exactly 16 hexadecimal characters (64 bits)
- **Valid hex characters**: 0-9, A-F (case insensitive)

## Files

- `des_server.py` - HTTP server implementing DES encryption/decryption (port 5000)
- `des_client.py` - Interactive HTTP client
- `desencryption_tugas2.py` - Original standalone DES implementation
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Notes

- The server uses Flask and runs on port 5000
- No administrator privileges required
- Suitable for educational purposes and development
- For production use, consider adding authentication and HTTPS

## Troubleshooting

### Localtunnel Connection Issues
- Make sure your server is running before starting localtunnel
- The server runs on port 5000 by default
- Some networks may block localtunnel connections
