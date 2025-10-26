# 🎉 SISTEM BERHASIL DIUBAH!

## Perubahan Utama

### ❌ Sebelum (Client-Server Biasa)
- Client kirim plaintext → Server encrypt → Return ciphertext
- Client lain tidak bisa akses hasil enkripsi
- Harus input hex format (16 chars)
- Key harus manual input

### ✅ Sekarang (Client-to-Client Communication)
- **Client 1** kirim text bebas → Server encrypt & simpan → Return Message ID
- **Client 2** gunakan Message ID → Server decrypt → Return plaintext
- **Plaintext bebas** - bisa teks apa saja!
- **Key otomatis** di-generate server

## 🚀 Cara Menggunakan

### Skenario: Kamu (Client 1) kirim pesan ke Teman (Client 2)

**Terminal 1 - Server:**
```bash
python des_server.py
```

**Terminal 2 - Kamu (Sender):**
```bash
python client_sender.py
```
- Server URL: `http://localhost:5000`
- Ketik pesan: "Halo! Besok jadi meet up jam 3 ya 😊"
- Dapat Message ID: `a7b3c2d1`
- **Share Message ID ke teman** (via WA/chat)

**Terminal 3 - Teman (Receiver):**
```bash
python client_receiver.py
```
- Server URL: `http://localhost:5000`
- Masukkan Message ID: `a7b3c2d1`
- **Lihat pesan terdekripsi!**

## 🌐 Remote Access (Localtunnel)

### Setup
```bash
# Terminal 1
python des_server.py

# Terminal 2
npm install -g localtunnel
lt --port 5000

# Copy URL: https://xyz.loca.lt
```

### Penggunaan
- **Kamu** (Client 1): Jalankan `client_sender.py`, gunakan URL localtunnel
- **Teman** (Client 2): Jalankan `client_receiver.py`, gunakan URL yang sama
- **Share Message ID** via chat
- Sekarang kalian bisa berkomunikasi dari jarak jauh!

## 📁 File Penting

| File | Fungsi |
|------|--------|
| `des_server.py` | Server dengan message storage |
| `client_sender.py` | Client 1 - Kirim pesan |
| `client_receiver.py` | Client 2 | Terima pesan |
| `test_client_communication.py` | Auto test script |
| `README_CLIENT.md` | Dokumentasi lengkap |

## 🔐 Fitur Keamanan

1. **DES Encryption**: Pesan di-encrypt dengan algoritma DES
2. **Auto Key Generation**: Key random untuk setiap pesan
3. **Message ID**: Hanya yang punya ID bisa decrypt
4. **Temporary Storage**: Pesan di memory (hilang saat server restart)

## 💡 Keunggulan

✅ **Free Text** - Tidak perlu format hex  
✅ **Auto Key** - Tidak perlu koordinasi key  
✅ **Message ID** - Mudah di-share  
✅ **Multi-Block** - Support pesan panjang  
✅ **Remote Ready** - Bisa via localtunnel  

## 🧪 Test Sistem

```bash
python test_client_communication.py
```

Script ini akan auto test:
1. Client 1 send message
2. Client 2 receive message
3. Verify plaintext matches
4. List all stored messages

## 📌 Catatan Penting

- **Server restart** = semua pesan hilang (in-memory storage)
- **Message ID** case-sensitive
- **Share Message ID** secara aman ke penerima
- **Localtunnel URL** bisa berubah setiap restart

## 🎓 Cocok Untuk

- Tugas kuliah enkripsi
- Demo komunikasi terenkripsi
- Belajar DES algorithm
- Praktik client-server architecture
- Understanding HTTP REST API

---

**Status**: ✅ READY TO USE!

Sistem sudah siap digunakan untuk komunikasi client-to-client dengan enkripsi DES! 🎉
