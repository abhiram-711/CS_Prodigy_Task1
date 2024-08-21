def encrypt(msg):
    output = ""
    for letter in msg:
        change = chr(ord(letter) + 3)
        output += change
    print("The Encrypted text is:", output)

def decrypt(msg):
    output = ""
    for letter in msg:
        change = chr(ord(letter) - 3)
        output += change
    print("The Decrypted text is:", output)

def main():
    while True:
        print("\nSelect options below:")
        print("Press 1 to Encrypt the plain text")
        print("Press 2 to Decrypt the text")
        print("Press 0 to Exit")

        user_input = input("Enter the option here: ")

        if user_input == '1':
            text = input("Enter the text to Encrypt: ")
            encrypt(text)
        elif user_input == '2':
            text = input("Enter the text to Decrypt: ")
            decrypt(text)
        elif user_input == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 0.")

if __name__ == "__main__":
    main()
