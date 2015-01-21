# Top Secret Encoder / Decoder
#
# This code is... broken!  (I don't know who wrote it.)
#
# Your challenge is to find the bug(s) and fix them, so that
# the program will properly encode any message and also
# decode it back to the original message.
#
# ---------------------------------------------------------------
#
# Here's how the encoder is supposed to work:
#
# 1. any uppercase letters should be considered lowercase
# 2. advance every letter by 3 places in the alphabet.
# 3. going past "z" should "rotate" back to to "a"
#
# The decoder function should reverse this process in order to
# recover the original message.
#
# Examples:
#
# hello  - should be encoded as -  khoor
# ZEBRA  - should be encoded as -  cheud
# Pizza  - should be encoded as -  slccd

def use_secret_encoder(plain_text):
  encoded_message = ""
  for letter in plain_text:
    new_letter = chr(ord(letter) + 3)
    encoded_message += new_letter
  return encoded_message

def use_secret_decoder(encoded_text):
  cipher_text = ""
  for letter in encoded_text:
  	new_letter = chr(ord(letter) - 3)
  	cipher_text += new_letter
  return cipher_text


message_to_be_encoded = input("What message do you want to send? ")
encrypted_message = use_secret_encoder(message_to_be_encoded)
print("Here's the encrypted version: ", encrypted_message)

plain_message = use_secret_decoder(encrypted_message)
print("Here's your original message: ", plain_message)
