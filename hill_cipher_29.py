alphanum = 'BCDEFGHIJKLMNOPQRSTUVWXYZA165'

List = dict(enumerate(alphanum))
rev_List = dict(zip(alphanum, range(len(alphanum))))

key_matrix = [[0]*3 for i in range(3)]


# Generate vector for the message
msg_vector = [[0] for i in range(3)]

#Generate matrix for the cipher
cipher_matrix = [[0] for i in range(3)]

#Function for generationg keymatrix from keystring

def get_key_matrix(key):
    k=0
    for i in range(3):
        for j in range(3):
            # key_matrix[i][j] =ord(key[k])%29
            key_matrix[i][j] = rev_List[key[k]]
            k +=1
    return key_matrix


def encrypt(messageVector):
	for i in range(3):
		for j in range(1):
			cipher_matrix[i][j] = 0
			for x in range(3):
				cipher_matrix[i][j] += (key_matrix[i][x] *
									messageVector[x][j])
			cipher_matrix[i][j] = cipher_matrix[i][j] % 29
			

def HillCipher(message, key):

	# Get key matrix from the key string
	get_key_matrix(key)

	# Generate vector for the message
	for i in range(3):
		msg_vector[i][0] = rev_List[message[i]] 

	# Following function generates
	# the encrypted vector
	encrypt(msg_vector)

	# Generate the encrypted text
	# from the encrypted vector
	CipherText = []
	for i in range(3):
		CipherText.append(List[cipher_matrix[i][0]])

	# Finally print the ciphertext
	print("Ciphertext: ", "".join(CipherText))


# y = int(input())
# print(List[])
# # x = input()
# # print(rev_List[x])

# key = 'FNCAWL165'

# print(get_key_matrix(key))



if __name__ == '__main__':
	message = "PAY"
	key = 'FNCAWL165'
	HillCipher(message, key)