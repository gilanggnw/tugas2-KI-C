# DES Client-to-Client Encrypted Communication

Sistem enkripsi DES yang memungkinkan **komunikasi antar client** secara aman melalui server.

## 🎯 Fitur Utama

- ✅ **Komunikasi Antar Client**: Client 1 kirim pesan terenkripsi → Client 2 decrypt
- ✅ **Auto-Generate Key**: Key DES di-generate otomatis oleh server
- ✅ **Free Text**: Plaintext bebas - tidak ada batasan format!
- ✅ **Message ID System**: Pesan disimpan dengan ID unik untuk sharing
- ✅ **Localtunnel Ready**: Bisa diakses dari internet

## 📋 Cara Kerja

```
┌─────────────────┐                                   ┌─────────────────┐
│   Client 1      │                                   │   Client 2      │
│   (Sender)      │                                   │   (Receiver)    │
└────────┬────────┘                                   └────────┬────────┘
         │                                                     │
         │ 1. POST /send                                      │
         │    {text: "Hello World"}                           │
         │                                                     │
         ▼                                                     │
    ┌────────────────────────────┐                           │
    │                            │                           │
    │   DES Server (Port 5000)   │                           │
    │                            │                           │
    │  • Generate random key     │                           │
    │  • Encrypt text dengan DES │                           │
    │  • Store encrypted message │                           │
    │  • Return message_id       │                           │
    │                            │                           │
    └────────┬───────────────────┘                           │
             │                                                 │
             │ 2. Response:                                    │
             │    {message_id: "abc123",                       │
             │     key: "..."}                                 │
             │                                                 │
             ▼                                                 │
    ┌─────────────────┐                                       │
    │  Share message  │                                       │
    │  ID to Client 2 ├──────────────────────────────────────►│
    └─────────────────┘                                       │
                                                               │
                                                               │ 3. POST /receive
                                                               │    {message_id: "abc123"}
                                                               │
                                                               ▼
                                          ┌────────────────────────────┐
                                          │   DES Server               │
                                          │                            │
                                          │  • Retrieve encrypted msg  │
                                          │  • Decrypt dengan key      │
                                          │  • Return plaintext        │
                                          │                            │
                                          └────────┬───────────────────┘
                                                   │
                                                   │ 4. Response:
                                                   │    {plaintext: "Hello World"}
                                                   │
                                                   ▼
                                          ┌─────────────────┐
                                          │  Client 2 reads │
                                          │  the message!   │
                                          └─────────────────┘
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start Server
```bash
python des_server.py
```

### 3. Client 1 (Sender) - Kirim Pesan

**Terminal baru:**
```bash
python client_sender.py
```

1. Masukkan server URL: `http://localhost:5000`
2. Pilih "Send a new message"
3. Ketik pesan apa saja (bebas!)
4. Copy **Message ID** yang diberikan

### 4. Client 2 (Receiver) - Terima Pesan

**Terminal baru:**
```bash
python client_receiver.py
```

1. Masukkan server URL: `http://localhost:5000`
2. Pilih "Receive a message"
3. Paste **Message ID** dari Client 1
4. Lihat pesan yang sudah di-decrypt!

## 🌐 Menggunakan Localtunnel (Remote Access)

### Setup Localtunnel

1. Install Node.js dari [nodejs.org](https://nodejs.org/)

2. Install localtunnel:
```bash
npm install -g localtunnel
```

3. Start server:
```bash
python des_server.py
```

4. Di terminal baru, jalankan localtunnel:
```bash
lt --port 5000
```

5. Copy URL yang diberikan (contoh: `https://xyz123.loca.lt`)

6. Gunakan URL tersebut di client:
   - Client 1 & 2 bisa di komputer berbeda
   - Gunakan localtunnel URL sebagai server URL
   - Sekarang kalian bisa berkomunikasi dari jarak jauh!

## 📡 API Endpoints

### POST /send
Kirim pesan terenkripsi (Client 1)

**Request:**
```json
{
  "text": "Pesan rahasia apapun!"
}
```

**Response:**
```json
{
  "status": "success",
  "message_id": "a1b2c3d4",
  "key": "ABCD1234567890EF",
  "plaintext": "Pesan rahasia apapun!",
  "encrypted_blocks": 2
}
```

### POST /receive
Terima dan decrypt pesan (Client 2)

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
  "plaintext": "Pesan rahasia apapun!",
  "key": "ABCD1234567890EF",
  "timestamp": "2025-10-26T10:30:00"
}
```

### GET /messages
Lihat semua pesan yang tersimpan

**Response:**
```json
{
  "status": "success",
  "total_messages": 5,
  "messages": [
    {
      "message_id": "a1b2c3d4",
      "timestamp": "2025-10-26T10:30:00",
      "blocks_count": 2,
      "sender_info": "Client 1"
    }
  ]
}
```

## 🔐 Cara Kerja Enkripsi

1. **Client 1 kirim plaintext** (bebas, bisa teks apa saja)
2. **Server convert** plaintext → hex blocks (16 chars per block)
3. **Server generate** random DES key (16 hex chars)
4. **Server encrypt** setiap block menggunakan DES
5. **Server simpan** encrypted blocks + key dengan message_id unik
6. **Client 1 share** message_id ke Client 2
7. **Client 2 request** dengan message_id
8. **Server decrypt** blocks menggunakan key yang sama
9. **Server return** plaintext original ke Client 2

## 📝 Contoh Penggunaan

### Skenario: Alice kirim pesan ke Bob

**Alice (Client 1):**
```bash
$ python client_sender.py
Server URL: http://localhost:5000
Message: Halo Bob! Kita meeting jam 3 ya.

✓ SUCCESS!
📋 MESSAGE ID: a7f3e2b1
🔑 KEY: 3F7A9E2C1B8D4E6F
Share this MESSAGE ID: a7f3e2b1
```

**Alice share ke Bob:** "Message ID: a7f3e2b1"

**Bob (Client 2):**
```bash
$ python client_receiver.py
Server URL: http://localhost:5000
Enter Message ID: a7f3e2b1

✓ SUCCESS! Message decrypted.
📄 ORIGINAL MESSAGE:
Halo Bob! Kita meeting jam 3 ya.
```

## 🛠 Troubleshooting

### Server tidak bisa diakses
- Pastikan server sedang running
- Check firewall settings
- Untuk localtunnel, pastikan port sama (5000)

### Message ID tidak ditemukan
- Pastikan Message ID benar (case-sensitive)
- Server menyimpan pesan di memory (hilang jika restart)

### Error saat install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 📂 File Structure

```
tugas2/
├── des_server.py           # Server dengan message storage
├── client_sender.py        # Client 1 (Pengirim)
├── client_receiver.py      # Client 2 (Penerima)
├── requirements.txt        # Dependencies
├── README_CLIENT.md        # This file
└── QUICKSTART.md          # Quick start guide
```

## 🎓 Educational Purpose

Sistem ini dibuat untuk tujuan edukasi:
- Memahami algoritma DES encryption
- Implementasi client-server communication
- Message passing antar client
- HTTP REST API

**⚠️ Catatan:** Untuk production, gunakan algoritma enkripsi modern (AES-256) dan tambahkan autentikasi!

## 💡 Tips

- Message disimpan di **memory** server (temporary)
- **Restart server** = semua pesan hilang
- **Share Message ID** via chat/WhatsApp ke penerima
- **Key otomatis** = tidak perlu koordinasi key manual
- **Free text** = bisa kirim pesan apa saja!

---

Selamat mencoba! 🚀
