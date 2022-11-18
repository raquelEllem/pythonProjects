# def encrypt(plain_text, shift_encrypt):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter) + shift_encrypt
#         if position > 25:
#             position -= 26
#         cipher_text += alphabet[position]
#     print(f"The encoded text is {cipher_text}")
#
#
# def decrypt(cipher_text, shift_decrypt):
#     decrypt_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter) - shift_decrypt
#         decrypt_text += alphabet[position]
#     print(f"The decoded text is {decrypt_text}")

import art08
def cesar(plain_text, shift_amount, direction_option):
    cipher_text = ""
    for letter in plain_text:
        if direction_option == "encode":
            position = alphabet.index(letter) + shift_amount
            if position > 25:
                position -= 26
            cipher_text += alphabet[position]
        elif direction_option == "decode":
            position = alphabet.index(letter) - shift_amount
            cipher_text += alphabet[position]
        else:
            print("Invalid option!")
            break
    print(f"The {direction_option}d text is {cipher_text}")

print(art08.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
cesar(plain_text=text, shift_amount=shift, direction_option=direction)
