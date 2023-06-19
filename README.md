# Image Encryption and Decryption using Hybrid AES-128 and ChaCha20 Cipher

This repository contains code for encrypting and decrypting images using a hybrid encryption scheme combining the AES-128 block cipher in CBC (Cipher Block Chaining) mode and the ChaCha20 stream cipher. The code is implemented in Python and utilizes the `pycryptodome` library for cryptographic operations.

## Features

- Encrypt an image using a hybrid encryption scheme combining AES-128 and ChaCha20 ciphers
- Utilized the pycryptodome library for cryptographic operations, ensuring reliable and efficient encryption and decryption processes.
- Contributed to image security by providing a practical solution for encrypting and decrypting images using hybrid encryption techniques.
- Save the encrypted and decrypted images in the same format as the original image

## Prerequisites

- Python 3.x
- `pycryptodome` library (can be installed using `pip install pycryptodome`)
- PIL (Python Imaging Library) library (can be installed using `pip install pillow`)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/meet2424/Hybrid-AES-128-and-ChaCha20-Cipher/ 
   ```

2. Place the image file (`original_image.jpeg`) that you want to encrypt/decrypt in the same directory as the code.

3. Open the `final.py` file and modify the `key` variable with a 32-byte key generated using `get_random_bytes()` (e.g., `key = get_random_bytes(32)`).

4. Run the `final.py` script:

   ```bash
   python final.py
   ```

5. The script will encrypt the image using a hybrid encryption scheme combining AES-128 CBC mode and ChaCha20 stream cipher. The encrypted image will be saved as `encrypted_image.jpeg` in the same directory.

6. The script will then decrypt the encrypted image using the same key and save the decrypted image as `decrypted_image.jpeg`.

7. The decrypted image will be identical to the original image.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
 
