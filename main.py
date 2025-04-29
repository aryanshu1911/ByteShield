import os
import json
import hashlib
from cryptography.fernet import Fernet

INTEGRITY_FILE = 'integrity.json'

# Generate encryption key
def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    try:
        return open('secret.key', 'rb').read()
    except Exception as e:
        print(f"✗ Error loading key: {e}")
        exit(1)

# Hashing function
def calculate_hash(file_path, algo='sha256'):
    hash_func = hashlib.new(algo)
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hash_func.update(chunk)
    return hash_func.hexdigest()

# Load or initialize integrity store
def load_integrity_store():
    if os.path.exists(INTEGRITY_FILE):
        with open(INTEGRITY_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_integrity_store(store):
    with open(INTEGRITY_FILE, 'w') as f:
        json.dump(store, f, indent=4)

# Encrypt a file
def encrypt_file(file_path, key):
    try:
        # Save hash before encryption
        hash_store = load_integrity_store()
        hash_store[file_path] = calculate_hash(file_path)  # Storing hash before encryption
        save_integrity_store(hash_store)
        
        fernet = Fernet(key)
        with open(file_path, 'rb') as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        print(f"✓ Encrypted: {file_path}")
    except Exception as e:
        print(f"✗ Failed to encrypt {file_path}: {e}")

# Decrypt a file and verify hash
def decrypt_file(file_path, key):
    try:
        fernet = Fernet(key)
        with open(file_path, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()

        # Attempt decryption
        decrypted = fernet.decrypt(encrypted)

        # Rewriting the decrypted content back to the file
        with open(file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)

        # Now, check the integrity of the decrypted file
        current_hash = calculate_hash(file_path)
        hash_store = load_integrity_store()
        original_hash = hash_store.get(file_path)

        # Check if hash is missing for this file
        if original_hash is None:
            print(f"⚠️ Integrity information missing for {file_path}.")
            user_input = input("Do you want to proceed with decryption anyway? (y/n): ").strip().lower()
            if user_input in ['y', 'yes']:
                print(f"✓ Decrypted: {file_path} (Warning: Missing hash)")
            else:
                print(f"✗ Decryption aborted for {file_path}.")
                return  # Exit decryption if user opts not to proceed

        # Check if the hash of the decrypted file matches the original hash
        elif original_hash != current_hash:
            print(f"⚠️ Integrity check failed for {file_path}. The file may have been tampered with.")
            user_input = input("Do you want to proceed with decryption anyway? (y/n): ").strip().lower()
            if user_input in ['y', 'yes']:
                print(f"✓ Decrypted: {file_path} (Warning: Hash mismatch)")
            else:
                print(f"✗ Decryption aborted for {file_path}.")
                return  # Exit decryption if user opts not to proceed

        # If integrity check passes, notify the user
        else:
            print(f"✓ Decrypted and verified: {file_path}")

    except Exception as e:
        print(f"✗ Failed to decrypt {file_path}: {e}")
 

# Folder operations
def encrypt_folder(folder_path, key):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename not in ['secret.key', INTEGRITY_FILE]:
            encrypt_file(file_path, key)

def decrypt_folder(folder_path, key):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename not in ['secret.key', INTEGRITY_FILE]:
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
            print("\n🛡️  ByteShield shutting down. Stay secure!\n")
            break
        else:
            print("✗ Invalid input! Please enter a number between 1 and 5.")

# Entry point
if __name__ == "__main__":
    main_menu()
