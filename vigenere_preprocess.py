#function to make a normal text into all capital 
#no punctuation . It needs to be between 350 and 500 words
import re
def makeupper(s):
    #s="sting. that'' has puncd!"
    s=re.sub(r'[^a-zA-z]','', s)
    s=s.upper()
    #print(s)
    return s



with open('smallplaintext.txt', 'r') as file:
    data=file.read().replace('\n','')
    print (type(data))
    #print (data)
    data_upper=makeupper(data)
    print (data_upper)


#write the clean all uppercase file
with open('clean_small_plaintext.txt', 'w') as file:
    file.write(data_upper)