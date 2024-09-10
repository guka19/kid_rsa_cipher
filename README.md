# RSA Encryption and Decryption Scripts
## This repository contains two Python scripts for demonstrating basic RSA encryption and decryption techniques.

RSA Basic Encryption/Decryption:

Script: rsa_basic.py
Functions:
calculate_n(e, d, M): Computes the modulus n.
encrypt(plaintext, e, n): Encrypts a plaintext integer.
decrypt(ciphertext, d, n): Decrypts a ciphertext integer.
Usage: This script allows encryption and decryption of an integer input using RSA parameters calculated from constants a, b, A, and B.
String Encryption/Decryption with Kid RSA:

Script: rsa_string.py
Functions:
string_to_int(s): Converts a string to an integer using ASCII values.
int_to_string(n): Converts an integer back to a string.
kid_rsa_setup(a, b, A, B): Sets up RSA parameters for encryption and decryption.
encrypt(x, e, n): Encrypts an integer.
decrypt(y, d, n): Decrypts an integer.
Usage: Demonstrates encryption and decryption of a string message by first converting it to an integer and back.
