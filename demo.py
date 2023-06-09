from Crypto.Cipher import AES
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    image = Image.open(image_path)
    width, height = image.size

    # Convert the image to RGB mode if it's not already
    image = image.convert('RGB')

    # Generate a random 128-bit IV for the block cipher mode
    iv = get_random_bytes(16)

    # Create a new image to store the encrypted pixels
    encrypted_image = Image.new('RGB', (width, height))

    # Use IV and key to encrypt each pixel using AES-128 in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            encrypted_pixel = cipher.encrypt(bytes(pixel)) 
            encrypted_image.putpixel((x, y), tuple(encrypted_pixel))

    return iv, encrypted_image

def decrypt_image(iv, encrypted_image, key):
    width, height = encrypted_image.size

    # Create a new image to store the decrypted pixels
    decrypted_image = Image.new('RGB', (width, height))

    # Use IV and key to decrypt each pixel using AES-128 in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    for y in range(height):
        for x in range(width):
            encrypted_pixel = encrypted_image.getpixel((x, y))
            decrypted_pixel = cipher.decrypt(encrypted_pixel)
            decrypted_image.putpixel((x, y), tuple(decrypted_pixel))

    return decrypted_image

key = get_random_bytes(16)
print("*****Image Encryption Using AES-128*****")
image_path = "sample1.png"
print("Encrypting Image.......")
iv, encrypted_image = encrypt_image(image_path, key)

encrypted_image_path = "encrypted_image.png"
encrypted_image.save(encrypted_image_path)

print("Decrypting Image.......")
decrypted_image = decrypt_image(iv, encrypted_image, key)

decrypted_image_path = "decrypted_image.png"
decrypted_image.save(decrypted_image_path)
