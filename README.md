# DES Client-to-Client Encrypted Communication

Sistem enkripsi DES yang memungkinkan **komunikasi antar client** secara aman melalui server dengan HTTP-based architecture.

## Features

- ✅ **Client-to-Client Communication** - Client 1 encrypt & send, Client 2 receive & decrypt
- ✅ **Auto Key Generation** - Server generates random DES key automatically
- ✅ **Free Text Input** - No hex format restriction, send any text!
- ✅ **Message ID System** - Share message ID to allow decryption
- ✅ **Localtunnel Compatible** - Access from anywhere via internet
- ✅ **RESTful API** - Clean HTTP endpoints
- ✅ **CORS Enabled** - Web access ready

## Quick Start

### Local Testing

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start server:
```bash
python des_server.py
```

3. Client 1 (Sender) - Send message:
```bash
python client_sender.py
```
Enter server URL: `http://localhost:5000`
Type your message and get Message ID

4. Client 2 (Receiver) - Receive message:
```bash
python client_receiver.py
```
Enter server URL: `http://localhost:5000`
Enter Message ID to decrypt message

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

## API Endpoints

### POST /send
Send encrypted message (Client 1)

**Request:**
```json
{
  "text": "Any message you want to send!"
}
```

**Response:**
```json
{
  "status": "success",
  "message_id": "a1b2c3d4",
  "key": "ABCD1234567890EF",
  "plaintext": "Any message you want to send!",
  "encrypted_blocks": 2
}
```

### POST /receive
Receive and decrypt message (Client 2)

**Request:**
```json
{
  "message_id": "a1b2c3d4"
}
```

**Response:**
```json
{
  "status": "success",
  "message_id": "a1b2c3d4",
  "plaintext": "Any message you want to send!",
  "key": "ABCD1234567890EF",
  "timestamp": "2025-10-26T10:30:00"
}
```

### GET /messages
List all stored messages

**Response:**
```json
{
  "status": "success",
  "total_messages": 5,
  "messages": [...]
}
```

## Testing with cURL

Test the API endpoints:

```bash
# Send message
curl -X POST http://localhost:5000/send \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello World!"}'

# Receive message (use message_id from above)
curl -X POST http://localhost:5000/receive \
  -H "Content-Type: application/json" \
  -d '{"message_id": "YOUR_MESSAGE_ID"}'

# List all messages
curl http://localhost:5000/messages
```

## Files

- `des_server.py` - HTTP server with message storage (port 5000)
- `client_sender.py` - Client 1 - Send encrypted messages
- `client_receiver.py` - Client 2 - Receive and decrypt messages  
- `test_client_communication.py` - Automated test script
- `desencryption_tugas2.py` - Original standalone DES implementation
- `requirements.txt` - Python dependencies

## How It Works

1. **Client 1** sends plaintext → Server generates key → Encrypts with DES → Stores with message_id
2. **Client 1** shares message_id with **Client 2**
3. **Client 2** requests with message_id → Server decrypts → Returns plaintext
4. **Auto key generation** - No manual key coordination needed
5. **Free text** - No hex format required, send any text!

## Troubleshooting

- **Cannot connect to server**: Make sure server is running and firewall allows port 5000
- **Message ID not found**: Server stores messages in memory (lost on restart)
- **Localtunnel issues**: Ensure server is running before starting localtunnel

---

**For detailed documentation, see [README_CLIENT.md](README_CLIENT.md)**  
**Quick start guide: [QUICKSTART.md](QUICKSTART.md)**
