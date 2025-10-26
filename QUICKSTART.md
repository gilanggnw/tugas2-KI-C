# Quick Start Guide - DES Client-to-Client Communication

## Konsep

Sistem ini memungkinkan **komunikasi antar client** melalui server:
- **Client 1 (Sender)**: Encrypt pesan → dapat Message ID
- **Client 2 (Receiver)**: Gunakan Message ID → decrypt pesan
- **Key otomatis di-generate** oleh server
- **Plaintext bebas** - bisa teks apa saja, tidak ada batasan!

```
Client 1 (Sender)          Server              Client 2 (Receiver)
      │                       │                         │
      │  POST /send          │                         │
      │  {text: "Hello"}     │                         │
      ├─────────────────────>│                         │
      │                       │ Generate key            │
      │                       │ Encrypt                 │
      │  {message_id: "abc"} │ Store                   │
      │<─────────────────────┤                         │
      │                       │                         │
      │  Share message_id     │                         │
      │──────────────────────────────────────────────>│
      │                       │                         │
      │                       │  POST /receive          │
      │                       │  {message_id: "abc"}    │
      │                       │<────────────────────────┤
      │                       │ Decrypt                 │
      │                       │ {plaintext: "Hello"}    │
      │                       ├────────────────────────>│
```

## Quick Start (3 Steps)

### 1. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 2. Start the Server

```powershell
python des_server.py
```

### 3. Test Communication

**Terminal 1 - Start Server:**
```powershell
python des_server.py
```

**Terminal 2 - Client 1 (Sender):**
```powershell
python client_sender.py
```
- Enter: `http://localhost:5000`
- Type your message (any text!)
- You'll get a **Message ID**

**Terminal 3 - Client 2 (Receiver):**
```powershell
python client_receiver.py
```
- Enter: `http://localhost:5000`
- Paste the **Message ID** from Client 1
- See the decrypted message!

---

## Using with Localtunnel (Remote Access)

### Prerequisites
- Node.js installed ([download here](https://nodejs.org/))

### Steps

1. **Install localtunnel** (one-time setup):
```powershell
npm install -g localtunnel
```

2. **Start the DES server**:
```powershell
python des_server.py
```

3. **Open a NEW terminal** and start localtunnel:
```powershell
lt --port 5000
```

You'll see output like:
```
your url is: https://your-random-name.loca.lt
```

4. **Client 1 (Sender)** - Kirim pesan:
```powershell
python client_sender.py
```
Enter localtunnel URL, then send your message

5. **Client 2 (Receiver)** - Terima pesan:
```powershell
python client_receiver.py
```
Enter localtunnel URL and Message ID to decrypt

---

## Quick Test

Test all endpoints automatically:
```powershell
python test_http_server.py
```

---

## API Examples

### Using curl

**Encrypt:**
```powershell
curl -X POST http://localhost:5000/encrypt -H "Content-Type: application/json" -d '{\"plaintext\": \"0123456789ABCDEF\", \"key\": \"133457799BBCDFF1\"}'
```

**Decrypt:**
```powershell
curl -X POST http://localhost:5000/decrypt -H "Content-Type: application/json" -d '{\"ciphertext\": \"85E813540F0AB405\", \"key\": \"133457799BBCDFF1\"}'
```

### Using PowerShell

**Encrypt:**
```powershell
$body = @{
    plaintext = "0123456789ABCDEF"
    key = "133457799BBCDFF1"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/encrypt" -Method Post -Body $body -ContentType "application/json"
```

**Decrypt:**
```powershell
$body = @{
    ciphertext = "85E813540F0AB405"
    key = "133457799BBCDFF1"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/decrypt" -Method Post -Body $body -ContentType "application/json"
```

---

## Troubleshooting

### "Port already in use"
Kill the process using port 5000:
```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill it (replace PID with actual process ID)
taskkill /PID <PID> /F
```

### "Cannot connect to server"
- Make sure the server is running
- Check firewall settings
- Verify the correct port number

### Localtunnel issues
- Make sure your server is running on port 5000
- Try a different port if 5000 is blocked
- Check your internet connection

---

## File Overview

| File | Purpose |
|------|---------|
| `des_server.py` | HTTP server with message storage (port 5000) |
| `client_sender.py` | Client 1 - Send encrypted messages |
| `client_receiver.py` | Client 2 - Receive and decrypt messages |
| `des_client.py` | Old client (legacy) |
| `requirements.txt` | Python dependencies |

---

## Next Steps

1. ✅ Install dependencies
2. ✅ Test locally
3. ✅ Set up localtunnel
4. ✅ Share your tunnel URL with others!

For more details, see `README.md`
