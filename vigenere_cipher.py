#Vegener cipher

def createKey(string, key):
    key = list(key)
    #the key in polyalphabet is a character of letters like Harriet. Harriet is a 7letter word.
    #So  if the string input e.g Newyork equals Harriet in number of digits, then return key.
    if len(string) == len(key):
        print(key)

    else:
        for i in range(len(string) -len(key)):# if string and keyword have different lengths, then find
            #the difference and thats the number of iterations in the loop.Each loop runs through 26rows.
            key.append(key[i % len(key)])
    return("". join(key))

def encryption(string, key):
    encrypt_text = []# is an arraylist.
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')# x is assigned to ordered list of alphabet.
        encrypt_text.append(chr(x))#whatever the ordered letter, it is added to encrypt_text.
    return("".join(encrypt_text))

def decryption(encrypt_text, key):
    source_text = []#is an arraylist
    for i in range(len(encrypt_text)):
        x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        source_text .append(chr(x))
    return("" . join(source_text))

string = input("Enter the message: ")
keyword = input("Enter the keyword: ")
key = createKey(string.upper(), keyword.upper())
encrypt_text = encryption(string.upper(),key.upper())#upper method is used so that decryption is done successfully
#incase user inputs string message in lowercase.
print("Encrypted message:", encrypt_text)
print("Decrypted message:", decryption(encrypt_text, key))

#when line breaks occur program automatically fills them with characters denoting the use of strips or replace functions.
