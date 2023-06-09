from Crypto.Cipher import AES
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
from PIL import Image 
import numpy as np
import io

def encrypt(plaintext, key):
    # Generate a random 128-bit IV for the block cipher mode
    iv = get_random_bytes(16)

    # Divide plaintext into blocks of 128 bits
    block_size = 16  # 16 bytes = 128 bits
    plaintext_blocks = [plaintext[i:i+block_size] for i in range(0, len(plaintext), block_size)]

    # Use IV and key to encrypt first plaintext block using AES-128 in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_blocks = [cipher.encrypt(plaintext_blocks[0])]

    # Use encrypted ciphertext and key to encrypt subsequent plaintext blocks using ChaCha20 stream cipher
    for i in range(1, len(plaintext_blocks)):
        cipher = ChaCha20.new(key=key, nonce=encrypted_blocks[-1][:12])
        encrypted_blocks.append(cipher.encrypt(plaintext_blocks[i]))

    # Combine encrypted ciphertext and IV
    encrypted_message = iv + b''.join(encrypted_blocks) 
    return encrypted_message

def decrypt(encrypted_message, key):
    # Split encrypted message into IV and encrypted ciphertext
    iv = encrypted_message[:16]
    encrypted_ciphertext = encrypted_message[16:]

    # Divide encrypted ciphertext into blocks of 128 bits
    block_size = 16  # 16 bytes = 128 bits
    encrypted_blocks = [encrypted_ciphertext[i:i+block_size] for i in range(0, len(encrypted_ciphertext), block_size)]

    # Use IV and key to decrypt first ciphertext block using AES-128 in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_blocks = [cipher.decrypt(encrypted_blocks[0])]

    # Use decrypted plaintext and key to decrypt subsequent ciphertext blocks using ChaCha20 stream cipher
    for i in range(1, len(encrypted_blocks)):
        cipher = ChaCha20.new(key=key, nonce=encrypted_blocks[i-1][:12])
        decrypted_blocks.append(cipher.decrypt(encrypted_blocks[i]))

    # Combine decrypted plaintext blocks
    plaintext = b''.join(decrypted_blocks) 
    return plaintext

key = get_random_bytes(32)
print("*****Image Encryption Using Hybrid AES-128 and ChaCha20 Cipher*****")
# image_path = "sample1.png"
# image = Image.open(image_path)
print("Encrypting Iamge.......")
img = np.array(Image.open("sample1.png"))
print("Pixels Array")
print(img)

to_string = ' '.join(map(str, img.flatten().tolist()))
print("Pixels")
print(to_string)
print("Bytes")
with open('sample1.png', "rb") as f:
    image_bytes = f.read() 
print(image_bytes)

encrypted_image_bytes = encrypt(to_string, key)
 
encrypted_image_path = "encrypted_image.bin"
with open(encrypted_image_path, "wb") as f:
    f.write(encrypted_image_bytes)
 
print("Decrypting Iamge.......")
  
decrypted_image_bytes = decrypt(encrypted_image_bytes, key)

decrypted_image_path = "decrypted_image.jpg"
with open(decrypted_image_path, "wb") as f:
    f.write(decrypted_image_bytes)
 