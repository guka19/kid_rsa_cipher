def calculate_n(e, d, M):
    """Calculate the value of n."""
    return int((e * d - 1) / M)

def encrypt(plaintext, e, n):
    """Encrypt the plaintext."""
    return (plaintext * e) % n

def decrypt(ciphertext, d, n):
    """Decrypt the ciphertext."""
    return (ciphertext * d) % n

def main():
    # Constants
    a, b, A, B = 3, 4, 5, 6
    M = a * b - 1
    e = A * M + a
    d = B * M + b
    n = calculate_n(e, d, M)

    print(f"Calculated values: M = {M}, e = {e}, d = {d}, n = {n}")

    # Encrypting the plaintext
    try:
        x = int(input("Enter your number to encrypt:\n"))
        encrypted = encrypt(x, e, n)
        print("Encrypted cipher text is:", encrypted)

        # Decrypting the ciphertext
        decrypted = decrypt(encrypted, d, n)
        print("Original plain text is:", decrypted)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
