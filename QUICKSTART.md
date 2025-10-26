# Quick Start Guide - DES HTTP Server with Localtunnel

## Quick Start (3 Steps)

### 1. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 2. Start the Server

```powershell
python des_server.py
```

### 3. Test Locally
Open a new terminal and run:
```powershell
python des_client.py
```
When prompted for server URL, enter: `http://localhost:5000`

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

4. **Use the client** with your localtunnel URL:
```powershell
python des_client.py
```
When prompted, enter: `https://your-random-name.loca.lt`

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
| `des_server.py` | HTTP server (port 5000) |
| `des_client.py` | Interactive HTTP client |
| `test_http_server.py` | Automated test suite |
| `desencryption_tugas2.py` | Original standalone implementation |
| `requirements.txt` | Python dependencies |

---

## Next Steps

1. ✅ Install dependencies
2. ✅ Test locally
3. ✅ Set up localtunnel
4. ✅ Share your tunnel URL with others!

For more details, see `README.md`
