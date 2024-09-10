# Step 1: Convert string to integer (ASCII values)
def string_to_int(s):
    return int(''.join(f'{ord(c):03}' for c in s))  # Convert each character to 3-digit ASCII

# Step 2: Convert integer back to string (after decryption)
def int_to_string(n):
    s = str(n)
    # Ensure the length of the string is a multiple of 3 (since each character is 3 digits)
    while len(s) % 3 != 0:
        s = '0' + s  # Pad with leading zeros
    return ''.join(chr(int(s[i:i+3])) for i in range(0, len(s), 3))  # Convert 3-digit groups back to characters

# Kid RSA Setup
def kid_rsa_setup(a, b, A, B):
    M = a * b - 1
    e = A * M + a
    d = B * M + b
    n = (e * d - 1) // M  # Floor division since n must be an integer
    return e, d, n

# Encryption function
def encrypt(x, e, n):
    return (x * e) % n

# Decryption function
def decrypt(y, d, n):
    return (y * d) % n

# Example usage

# Step 3: Setup Kid RSA (Alice chooses a, b, A, B)
a, b, A, B = 30, 40, 50, 60
e, d, n = kid_rsa_setup(a, b, A, B)

# Step 4: Encrypt a message
message = "Hi"
x = string_to_int(message)
print(f"Original message: {message}")
print(f"Converted to integer: {x}")

# Check if x < n
if x >= n:
    raise ValueError("Message integer is too large for encryption. Choose larger n or shorter message.")

# Encrypt the integer
ciphertext = encrypt(x, e, n)
print(f"Ciphertext: {ciphertext}")

# Step 5: Decrypt the ciphertext
decrypted_x = decrypt(ciphertext, d, n)
print(f"Decrypted integer: {decrypted_x}")

# Convert back to string
decrypted_message = int_to_string(decrypted_x)
print(f"Decrypted message: {decrypted_message}")
