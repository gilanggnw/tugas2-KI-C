# DES Client-to-Client Communication - Project Structure

```
tugas2/
│
├── 📄 Core Files
│   ├── des_server.py              # Main HTTP server with message storage
│   ├── client_sender.py           # Client 1 - Send encrypted messages
│   ├── client_receiver.py         # Client 2 - Receive and decrypt messages
│   └── desencryption_tugas2.py    # Original standalone DES implementation
│
├── 🧪 Testing
│   └── test_client_communication.py   # Automated test suite
│
├── 📚 Documentation
│   ├── README.md                  # Main documentation (this file)
│   ├── README_CLIENT.md           # Detailed client-to-client guide
│   ├── QUICKSTART.md              # Quick start guide
│   └── SUMMARY.md                 # Summary of changes
│
├── ⚙️ Configuration
│   ├── requirements.txt           # Python dependencies
│   └── .gitignore                 # Git ignore rules
│
└── 📁 Generated (gitignored)
    └── __pycache__/              # Python cache files
```

## File Descriptions

### Core Files

**`des_server.py`** (Main Server)
- Flask HTTP server on port 5000
- Endpoints: `/send`, `/receive`, `/messages`
- Auto key generation
- In-memory message storage
- CORS enabled

**`client_sender.py`** (Client 1)
- Interactive sender interface
- Send free-text messages
- Get message ID for sharing
- View all stored messages

**`client_receiver.py`** (Client 2)
- Interactive receiver interface
- Decrypt messages using message ID
- View message details
- List available messages

**`desencryption_tugas2.py`** (Legacy)
- Original DES implementation
- Standalone encryption/decryption
- Educational reference

### Testing

**`test_client_communication.py`**
- Automated testing script
- Tests send → receive flow
- Verifies encryption/decryption
- Checks message listing

### Documentation

**`README.md`**
- Project overview
- Quick start guide
- API documentation
- Basic usage

**`README_CLIENT.md`**
- Detailed client-to-client guide
- Architecture explanation
- Localtunnel setup
- Complete examples

**`QUICKSTART.md`**
- Step-by-step quick start
- Local and remote usage
- Troubleshooting

**`SUMMARY.md`**
- Summary of changes
- Before/after comparison
- Key features

### Configuration

**`requirements.txt`**
- Flask==3.0.0
- flask-cors==4.0.0
- requests==2.31.0

**`.gitignore`**
- Python cache files
- Virtual environments
- IDE settings
- OS-specific files

## Usage Flow

```
1. Start Server
   └─> python des_server.py

2. Client 1 (Sender)
   └─> python client_sender.py
       └─> Enter message
       └─> Get message_id
       └─> Share message_id

3. Client 2 (Receiver)
   └─> python client_receiver.py
       └─> Enter message_id
       └─> See decrypted message
```

## Removed Files (Cleanup)

These files were removed as they are no longer needed:
- ❌ `des_client.py` - Replaced by `client_sender.py` and `client_receiver.py`
- ❌ `test_http_server.py` - Replaced by `test_client_communication.py`
- ❌ `test_tcp_des.py` - Old TCP version (not needed for HTTP)
- ❌ `test_input.txt` - Sample input (not needed)

## Dependencies

All Python dependencies are in `requirements.txt`:
```bash
pip install -r requirements.txt
```

For localtunnel (remote access):
```bash
npm install -g localtunnel
```

---

**Total Files**: 12 (clean and organized!)
