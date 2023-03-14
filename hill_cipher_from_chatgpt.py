key = 'BCDEFGHIJKLMNOPQRSTUVWXYZA165'
key_matrix = [[0 for i in range(3)] for j in range(3)]
# get_key_matrix(key)

def encrypt(plaintext, key_matrix):
    ciphertext = ''
    n = len(key_matrix)
    for i in range(0, len(plaintext), n):
        # Create the vector from the plaintext block
        vector = [ord(c) % 65 for c in plaintext[i:i+n]]
        # Pad the vector with zeros if necessary
        while len(vector) < n:
            vector.append(0)
        # Multiply the vector by the key matrix
        result = [sum([key_matrix[i][j] * vector[j] for j in range(n)]) % 26 for i in range(n)]
        # Convert the result to a string of characters
        ciphertext += ''.join([chr(c + 65) for c in result])
    return ciphertext

# def decrypt(ciphertext, key_matrix):
#     plaintext = ''
#     n = len(key_matrix)
#     # Compute the inverse of the key matrix
#     det = (key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]) % 26
#     det_inv = pow(det, -1, 26)
#     inv_matrix = [[0 for i in range(n)] for j in range(n)]
#     inv_matrix[0][0] = (key_matrix[1][1] * det_inv) % 26
#     inv_matrix[1][1] = (key_matrix[0][0] * det_inv) % 26
#     inv_matrix[0][1] = (-key_matrix[0][1] * det_inv) % 26
#     inv_matrix[1][0] = (-key_matrix[1][0] * det_inv) % 26
#     # Decrypt each block of the ciphertext
#     for i in range(0, len(ciphertext), n):
#         # Create the vector from the ciphertext block
#         vector = [ord(c) % 65 for c in ciphertext[i:i+n]]
#         # Multiply the vector by the inverse of the key matrix
#         result = [sum([inv_matrix[i][j] * vector[j] for j in range(n)]) % 26 for i in range(n)]
#         # Convert the result to a string of characters
#         plaintext += ''.join([chr(c + 65) for c in result])
#     return plaintext



