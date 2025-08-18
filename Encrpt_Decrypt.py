from cryptography.fernet import Fernet

Key = Fernet.generate_key()

cipher = Fernet(Key)


def encrypt_text(text):
    encrypted = cipher.encrypt(text.encode())
    return encrypted


def decrypt_text(token):
    decrypted = cipher.decrypt(token).decode()
    return decrypted

if __name__ == "__main__":
    print("Genreated key : ", Key.decode())

    while True:
        choice = int(input("Choose the following option :\n1. Encrypt text\n2. Decrypt Text\n3. Exit\nEnter : "))

        if(choice == 1):
            text = input("Enter text to encrypt: ")

            encrypted_text = encrypt_text(text)
            print("\nEncrypted:", encrypted_text.decode())
        
        elif(choice == 2):
            inp = input("Enter text to decrypt: ")

            decrypted_text = decrypt_text(inp)
            print("\nDecrypted:", decrypted_text)

        elif(choice==3):
            break

        else:
            print("Invalid choice !!!! You can only enter number between 1,2 and 3.....")
