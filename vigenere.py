import matplotlib.pyplot as plt

def openCiphertext(text):
    with open(text, 'r') as f:
        mytext=f.read()
    return mytext


## opens the clean plaintext (all caps only a-z)
def openPlaintext(text):
    with open(text, 'r') as f:
        mytext=f.read()
        return mytext


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
    with open('ciphertext3.txt', 'w') as myfile:
        myfile.write(encrypt(plaintext=plaintext,key=key))


## used to create our cipher
# key1='JQOTNXIZ'
# plaintext=openPlaintext()
# print( plaintext)
# encrypt_to_txt(plaintext=plaintext,key=key1)


def decrypt(ciphertext,key):
    plaintext=''
    for i in range(len(ciphertext)):
        c=alphabet.index(ciphertext[i])
        k=alphabet.index(key[i%len(key)])
        plainnumber=(c-k)%26
        plaincharacter=alphabet[plainnumber]
        plaintext+=plaincharacter
    return plaintext

def decrypt_to_txt(ciphertext,key):
    with open('possible_decrypted.txt', 'w') as myfile:
        myfile.write(decrypt(ciphertext=ciphertext,key=key))


englishLetterFreqDict = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

def getLetterCount(msg):
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    
    msg=msg.upper()
    for letter in msg:
        if letter in alphabet:
            letterCount[letter]+=1
    return letterCount



def getFrequencyOrder(letterCount):
    sortedFreq=sorted(letterCount.items(), key=lambda x:x[1], reverse=True)
    sortedDictFreq=dict(sortedFreq)
    return sortedDictFreq

def indexOfCoincidence(msg):
    counts=[0]*26
    for c in msg:
        counts[alphabet.index(c)]+=1
    n=0
    tot=0

    for i in range(26):
        n+=counts[i]*(counts[i]-1)
        tot+=counts[i]
    return 26*n/(tot*(tot-1))



ciphertext=openCiphertext('cipher.txt')
found=False
period=0
while not found:
    period+=1
    slices=['']*period
    print (period, slices)
    for i in range(len(ciphertext)):
        #keep only the period-th occurence od the ciphertext
        slices[i%period]+=ciphertext[i]
    print(slices)
    suma=0
    for i in range(period):
        suma+=indexOfCoincidence(slices[i])
        coincidence=suma/period
        if coincidence>1.6:
            found=True
print("The key has : {0} characters".format(period))


## all characters in a slice were encoded using the same letter#
## a slice is just a rotation cipher
## check frequency of letters because we cannot look at words

from math import sqrt
def findCosine(x,y):
    num=0
    x_squared=0
    y_squared=0
    for i in range(len(x)):
        num+=x[i]*y[i]
        x_squared+=x[i]*x[i]
        y_squared+=y[i]*y[i]
    return num/ sqrt(x_squared*y_squared)

def alphabeticOrder(diction):
    return dict(sorted(diction.items()))

## a dictionary in alphabetic order with the frequencies of the english language
sortedLangFreqDict=alphabeticOrder(englishLetterFreqDict)
listSortedLangFreqDict=list(sortedLangFreqDict.values())

## gets the frequencies for the entries in a text
# print(list(sortedLangFreqDict.values()))
cosinePerLetter={}
for z in range(len(slices)):
    cosinePerLetter[z]={}
    
    for potentialKey in alphabet:
        
        decryptedSlice=decrypt(slices[z], potentialKey) 
        print("for character {0} the frequency is: ". format(potentialKey))
        letterCount=getLetterCount(decryptedSlice)
        listLetterCount=list(letterCount.values())
        freqListLetterCount=[round(100*x/sum(listLetterCount),2) for x in listLetterCount]
        print(getFrequencyOrder(letterCount))
        #print(freqListLetterCount)
        cos=findCosine(listSortedLangFreqDict,freqListLetterCount)
        print("the cosine is: {}".format(cos))
        cosinePerLetter[z][potentialKey]=cos
        print("\n")
    
    
for _ in range(len(cosinePerLetter)):

    print(dict(sorted(cosinePerLetter[_].items(), key=lambda x: x[1],reverse=True)))
    print("\n")

decrypt_to_txt(ciphertext,'AVOCADO')