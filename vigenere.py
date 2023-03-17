
#open the non encrypted file
with open('clean_plaintext.txt', 'r') as f:
    mytext=f.read()
    print(mytext)

# zero based 
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(plaintext,key):
    #assume the key is 4-8 characters long
    ciphertext=''
    #go through it character by character
    for i in range (len(plaintext)):
        #get the character in the plaintext
        #and find the position in the alphabet
        p=alphabet.index(plaintext[i])

        #get the character in the key
        #and find the position in the alphabet
        #modulo len(key) since the key is repeated
        k=alphabet.index(key[i%(len(key))])
        
        ciphernumber=(p+k)%26
        ciphercharacter=alphabet[ciphernumber]
        ciphertext+=ciphercharacter
    return ciphertext

def encrypt_to_txt(plaintext,key):
    with open('ciphertext.txt', 'w') as myfile:
        myfile.write(encrypt(plaintext=plaintext,key=key))

encrypt_to_txt(mytext,'LEMON')




