#Nabodip Thapa
import string
characters = string.ascii_uppercase + string.ascii_uppercase
def welcome():
    print('Welcome to the Caesar Cipher')
    print("This program encrypts and decrypts text with the Casesar Cipher.")
def enter_message():
    while True:
        user = input("Would you like to encrypt (en) or decrypt (de):")
        if user == 'en':
            encrypt()
            break
        elif user == 'de':
            decrypt()
            break
        else:
            print("Invalid Mode")
            continue
def encrypt():
    encrypt = list(input("What message would you like to encrypt: ").upper())
    while True:
        shift = input("What is the shift number: ")
        if shift.strip().isdigit():
            shift = int(shift)
            break
        else:
            print("Invalid shift")
            continue
    for i in range(len(encrypt)):
        if encrypt[i] == ' ':
            encrypt[i] == ' '
        else:
            res = characters.index(encrypt[i]) + shift
            encrypt[i] = characters[res]
    print(''.join(map(str, encrypt)))
def decrypt():
    decrypt = list(input("What message would you like to decrypt: ").upper())
    while True:
        shift = input("What is the shift number: ")
        if shift.strip().isdigit():
            shift = int(shift)
            break
        else:
            print("Invalid shift")
            continue
    for i in range(len(decrypt)):
        if decrypt[i] == ' ':
            decrypt[i] = ' '
        else:
            res = characters.index(decrypt[i]) - shift
            decrypt[i] = characters[res]

    print(''.join(map(str, decrypt)))
welcome()
enter_message()
while True:
    re = input("Would you like to encrypt or decrypt another message? (yes/no): ")
    if re == 'yes':
        enter_message()
    elif re == 'no':
        print("Goodbye, and thanks for using the program!")
        break
    else:
        continue
