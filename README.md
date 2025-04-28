# ByteShield
 AES-based symmetric data encryption and decryption

**ByteShield** is a powerful file encryption and decryption utility that uses AES-based **Fernet** symmetric encryption. It allows you to easily protect and secure your files and folders by encrypting them with a strong key, ensuring that your sensitive data is safe from unauthorized access.

## Features

- **AES-based encryption**: Uses the **Fernet** algorithm to securely encrypt and decrypt files.
- **Encrypt individual files**: Protect specific files with a password (encryption key).
- **Encrypt entire folders**: Batch-encrypt all files in a folder to protect them.
- **Decrypt files/folders**: Easily decrypt files and folders that were previously encrypted.
- **Simple user interface**: Command-line interface with easy-to-follow prompts.

## Usage
### Step 1: Generate Encryption Key
The first time you run **ByteShield**, a secret key will be generated. This key is used for encryption and decryption of files.
To generate the key, simply run the program and it will automatically create a **`secret.key`** file. This key file should be kept safe!

### Step 2: Encrypt a File
To encrypt a file:
1. Run the script.
2. Select option **1** to encrypt a file.
3. Enter the full path of the file to encrypt.
4. The file will be encrypted and saved.

### Step 3: Decrypt a File
To decrypt a file:
1. Run the script.
2. Select option **2** to decrypt a file.
3. Enter the full path of the file to decrypt.
4. The file will be decrypted and restored.

### Step 4: Encrypt All Files in a Folder
To encrypt all files in a folder:
1. Run the script.
2. Select option **3** to encrypt all files in a folder.
3. Provide the folder path where your files are located.
4. All files in the folder (except the `secret.key`) will be encrypted.

### Step 5: Decrypt All Files in a Folder
To decrypt all files in a folder:
1. Run the script.
2. Select option **4** to decrypt all files in a folder.
3. Provide the folder path where the encrypted files are located.
4. All encrypted files will be decrypted and restored.

### Step 6: Exit
To exit the tool, simply select option **5** to safely shut down the application.

## Key Concepts

- **Encryption Key**: The key used to encrypt and decrypt files. It is important to keep the key safe, as losing it will prevent you from accessing your encrypted files.
- **AES-based Encryption**: AES (Advanced Encryption Standard) is one of the most secure encryption algorithms available. **Fernet** is a specific implementation of AES for symmetric encryption (same key for encryption and decryption).
  
## Security Considerations
- **Keep the key file safe**: The **`secret.key`** file is critical for decrypting your files. If you lose it, you will not be able to decrypt your files.
- **Password Protection**: The encryption key should be stored securely and not shared carelessly.

## License
This project is licensed under the **MIT License** 
