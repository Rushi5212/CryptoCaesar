# Caesar Cipher Encryption-Decryption in Python

This is a simple Python program that implements the **Caesar Cipher** encryption and decryption. The user can enter a message and a shift value, and the program will display the original message, the encrypted message, and the decrypted message.

## 📌 Features
- Encrypts a message using the Caesar Cipher technique.
- Decrypts the encrypted message back to its original form.
- Handles both uppercase and lowercase letters.
- Keeps spaces and special characters unchanged.

## 🚀 How It Works
1. The user enters a message and a shift value.
2. The program encrypts the message by shifting letters forward.
3. The program decrypts the message by shifting letters backward.
4. The results are displayed.

## 🔧 Usage
### Run the script:
```bash
python caesar_cipher.py



Example:

Enter your message: Hello World!
Enter shift value: 3

Original Message: Hello World!
Encrypted Message: Khoor Zruog!
Decrypted Message: Hello World!
🛠️ Code Overview

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if encrypt else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char
    return result
📜 License
This project is open-source and available under the MIT License.

💡 Contributions
Feel free to contribute by improving the code, adding new features, or fixing issues. Pull requests are welcome! 🚀

📬 Contact
If you have any questions, feel free to reach out!
Email: rushikeshchaudhari124@gmail.com



You can modify the contact details before uploading. Let me know if you need any changes! 🚀






