def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if encrypt else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char  # Keep spaces and special characters unchanged
    return result

# Get input from user
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

# Encrypt the message
encrypted_message = caesar_cipher(message, shift, encrypt=True)
# Decrypt the message
decrypted_message = caesar_cipher(encrypted_message, shift, encrypt=False)

# Display results
print(f"\nOriginal Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")
