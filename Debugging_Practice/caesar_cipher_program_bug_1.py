"""
    Module Lab 6: Caesar Cipher Program Bug #1

    In Module Lab 4, you created a Caesar Ciper program. This version of
    the program is bugging. Use a debugger to find the bug and fix it.
"""

def get_double_alphabet(alphabet):
    """
     Double the given alphabet.
    """
    double_alphabet = alphabet + alphabet
    return double_alphabet

def get_message():
    """
     Get a message to encrypt.
    """
    string_to_encrypt = input("Please enter a message to encrypt: ")
    return string_to_encrypt

def get_cipher_key():
    """
     Get a cipher key.
    """
    shift_amount = input("Please enter a key (whole number from 1-25): ")
    return shift_amount

def encrypt_message(message, cipher_key, alphabet):
    """
     Encrypt Message
    """
    encrypted_message = ""
    uppercase_message = ""
    uppercase_message = message.upper()
    for current_character in uppercase_message:
        position = alphabet.find(current_character)
        new_position = position + cipher_key
        if current_character in alphabet:
            encrypted_message = encrypted_message + alphabet[new_position]
        else:
            encrypted_message = encrypted_message + current_character
    return encrypted_message

def decrypt_message(message, cipher_key, alphabet):
    """
     Decrypt Message
    """
    decrypt_key = -1 * int(cipher_key)
    return encrypt_message(message, decrypt_key, alphabet)

def run_caesar_cipher_program():
    """
     Main program logic.
    """
    my_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {my_alphabet}')
    my_alphabet2 = get_double_alphabet(my_alphabet)
    print(f'Alphabet2: {my_alphabet2}')
    my_message = get_message()
    print(my_message)
    my_cipher_key = get_cipher_key()
    print(my_cipher_key)
    my_encrypted_message = encrypt_message(my_message, my_cipher_key, my_alphabet2)
    print(f'Encrypted Message: {my_encrypted_message}')
    my_decrypted_message = decrypt_message(my_encrypted_message, my_cipher_key, my_alphabet2)
    print(f'Decrypted Messgae: {my_decrypted_message}')

# Main Logic
run_caesar_cipher_program()