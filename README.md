# ByteShield  
🛡️ AES-Based Symmetric Data Encryption with Integrity Verification

**ByteShield** is a robust file encryption and decryption tool powered by **Fernet** (AES-based symmetric encryption). In addition to encrypting files and folders, ByteShield now also tracks file integrity using SHA-256 hashes—ensuring your data is not only encrypted, but also verifiably unchanged.

---

## 🔐 Features

- **AES-based encryption**: Utilizes **Fernet**, an AES symmetric encryption method for strong security.
- **File integrity verification**: Stores and verifies hashes to detect tampering during decryption.
- **Encrypt individual files**: Lock down specific files securely.
- **Encrypt entire folders**: Batch-process folders for mass encryption.
- **Decrypt with verification**: Ensures decrypted files match their original hash.
- **Command-line interface**: Intuitive prompts for smooth operation.

---

## 🚀 Getting Started

### Step 1: Generate an Encryption Key
The first time you run ByteShield, it automatically creates a `secret.key` file. This file is essential for encryption and decryption.

```
secret.key  ➜  DO NOT delete or lose this file!
```

---

### Step 2: Encrypt a File
1. Run the script.
2. Choose **1** to encrypt a file.
3. Enter the full file path.
4. ByteShield encrypts the file and saves its original hash for future verification.

---

### Step 3: Decrypt a File
1. Run the script.
2. Choose **2** to decrypt a file.
3. Enter the encrypted file’s full path.
4. ByteShield decrypts the file and:
   - Verifies its hash if available.
   - Warns if the hash is missing or doesn't match.

---

### Step 4: Encrypt All Files in a Folder
1. Choose **3** from the menu.
2. Provide the folder path.
3. All files in the folder (excluding `secret.key` and `integrity.json`) are encrypted and logged for integrity.

---

### Step 5: Decrypt All Files in a Folder
1. Choose **4** from the menu.
2. Provide the folder path.
3. ByteShield decrypts all files, checking their original hashes.

---

### Step 6: Exit
Choose **5** to close the application safely.

---

## 🔒 File Integrity Protection

- A file's hash is saved before encryption in an `integrity.json` file.
- Upon decryption, the file is rehashed and compared to its stored value.
- If a mismatch is found or no hash is available, you’ll be prompted to confirm before continuing.

---

## ⚠️ Security Notes

- **Keep `secret.key` safe** — without it, decryption is impossible.
- **Protect `integrity.json`** — tampering with it may result in integrity verification failures.
- Avoid modifying files manually while encrypted or decrypted.

---

## 📂 Files Created by ByteShield

| File             | Purpose                                     |
|------------------|---------------------------------------------|
| `secret.key`     | Holds the encryption/decryption key         |
| `integrity.json` | Stores SHA-256 hashes of original file data |

---

## 🧑‍💻 License

This project is licensed under the **MIT License**.  
