# Encrypt/decrypt files using Fernet (AES-based symmetric encryption)

import os
from cryptography.fernet import Fernet

# Generate encryption key and save it to a file
def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

# To load the key from file
def load_key():
    try:
        return open('secret.key', 'rb').read()
    except Exception as e:
        print(f"Error loading key: {e}")
        exit(1)

# To encrypt a single file
def encrypt_file(file_path, key):
    try:
        fernet = Fernet(key)
        with open(file_path, 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)   # Encrypts the raw data
        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
        print(f"Encrypted: {file_path}")
    except Exception as e:
        print(f"Failed to encrypt {file_path} : {e}")

# To decrypt a single file
def decrypt_file(file_path, key):
    try:
        fernet = Fernet(key)
        with open(file_path, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
        decrypted = fernet.decrypt(encrypted)   # Decrypts the encrypted data
        with open(file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
        print(f"Decrypted: {file_path}")
    except Exception as e:
        print(f"Failed to decrypt {file_path} : {e}")
    
# To encrypt all files in a folder
def encrypt_folder(folder_path, key):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename != "secret.key":
            encrypt_file(file_path, key)

# To decrypt all files in a folder
def decrypt_folder(folder_path, key):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename != "secret.key":
            decrypt_file(file_path, key)

# Main Menu (User Interface)
def main_menu():
    print(r"""
  ╔════════════════════════════════════════════════╗
  ║        🔐 ByteShield File Vault v1.0          ║
  ║   AES-powered encryption & decryption utility  ║
  ╚════════════════════════════════════════════════╝
    """)

    if not os.path.exists("secret.key"):
        generate_key()
    
    key = load_key()

    while True:
        print("\n=== File Encryption Tool ===")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Encrypt all files in a folder")
        print("4. Decrypt all files in a folder")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            file_path = input("Enter the full path of the file to encrypt: ").strip()
            if os.path.isfile(file_path):
                encrypt_file(file_path, key)
            else:
                print("Invalid file path.")
        elif choice == '2':
            file_path = input("Enter the full path of the file to decrypt: ").strip()
            if os.path.isfile(file_path):
                decrypt_file(file_path, key)
            else:
                print("Invalid file path.")
        elif choice == '3':
            folder_path = input("Enter the folder path to encrypt all files: ").strip()
            if os.path.isdir(folder_path):
                encrypt_folder(folder_path, key)
            else:
                print("Invalid folder path.")
        elif choice == '4':
            folder_path = input("Enter the folder path to decrypt all files: ").strip()
            if os.path.isdir(folder_path):
                decrypt_folder(folder_path, key)
            else:
                print("Invalid folder path.")
        elif choice == '5':
            print("🛡️  Encryption tool shutting down. Stay secure!")
            break
        else:
            print("Invalid input! Please enter a number between 1 and 5.")

# Entry point
if __name__ == "__main__":
    main_menu() 
