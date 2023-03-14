alphanum = 'BCDEFGHIJKLMNOPQRSTUVWXYZA165'

List = enumerate(alphanum)
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
            key_matrix[i][j] =ord(key[k])%65
            k +=1