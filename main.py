# Encrypt/decrypt files using Fernet (AES-based symmetric encryption)

import os
from cryptography.fernet import Fernet

# Generate encryption key and save it to a file
def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

# Load the key from file
def load_key():
    try:
        return open('secret.key', 'rb').read()
    except Exception as e:
        print(f"✗ Error loading key: {e}")
        exit(1)

# Encrypt a single file
def encrypt_file(file_path, key):
    try:
        fernet = Fernet(key)
        with open(file_path, 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
        print(f"✓ Encrypted: {file_path}")
    except Exception as e:
        print(f"✗ Failed to encrypt {file_path}: {e}")

# Decrypt a single file
def decrypt_file(file_path, key):
    try:
        fernet = Fernet(key)
        with open(file_path, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
        decrypted = fernet.decrypt(encrypted)
        with open(file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
        print(f"✓ Decrypted: {file_path}")
    except Exception as e:
        print(f"✗ Failed to decrypt {file_path}: {e}")

# Encrypt all files in a folder
def encrypt_folder(folder_path, key):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename != "secret.key":
            encrypt_file(file_path, key)

# Decrypt all files in a folder
def decrypt_folder(folder_path, key):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename != "secret.key":
            decrypt_file(file_path, key)

# Main Menu (User Interface)
def main_menu():
    print(r"""
  ╔════════════════════════════════════════════╗
  ║       🛡️  ByteShield File Vault v1.0        ║
  ║   ───────────────────────────────────────  ║
  ║   🔐 AES-powered encryption & decryption   ║
  ║   🚨 Lock Down Your Data, ⚔️  Encrypt Now   ║
  ╚════════════════════════════════════════════╝
    """)


    if not os.path.exists("secret.key"):
        print("🔑 No key found. Generating a new one...")
        generate_key()
    
    key = load_key()

    while True:
        print("\n==== ByteShield v1.0 Control Panel ====\n")
        print("1. 🔒 Encrypt a file")
        print("2. 🔓 Decrypt a file")
        print("3. 🗂️  Encrypt all files in a folder")
        print("4. 📁 Decrypt all files in a folder")
        print("5. ❌ Exit")

        choice = input("\n➡️  Enter your choice (1-5): ").strip()
        
        if choice == '1':
            file_path = input("📝 Enter the full path of the file to encrypt: ").strip()
            if os.path.isfile(file_path):
                encrypt_file(file_path, key)
            else:
                print("✗ Invalid file path.")
        elif choice == '2':
            file_path = input("📝 Enter the full path of the file to decrypt: ").strip()
            if os.path.isfile(file_path):
                decrypt_file(file_path, key)
            else:
                print("✗ Invalid file path.")
        elif choice == '3':
            folder_path = input("📝 Enter the folder path to encrypt all files: ").strip()
            if os.path.isdir(folder_path):
                encrypt_folder(folder_path, key)
            else:
                print("✗ Invalid folder path.")
        elif choice == '4':
            folder_path = input("📝 Enter the folder path to decrypt all files: ").strip()
            if os.path.isdir(folder_path):
                decrypt_folder(folder_path, key)
            else:
                print("✗ Invalid folder path.")
        elif choice == '5':
            print("\n🛡️  ByteShield shutting down. Stay secure! ")
            print()
            break
        else:
            print("✗ Invalid input! Please enter a number between 1 and 5.")

# Entry point
if __name__ == "__main__":
    main_menu()
