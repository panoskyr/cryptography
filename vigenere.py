#function to make a normal text into all capital 
#no punctuation . It needs to be between 350 and 500 words
import re
def makeupper(s):
    s="sting. that'' has puncd!"
    s=re.sub(r'[^\w]','', s)
    s=s.upper()
    print(s)
    return s
