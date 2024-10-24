import string

alphabet = string.ascii_lowercase
print(alphabet)

def ecnrypt(strToEcnrypt,key):
    encrypted = ""

    for char in strToEcnrypt:
        char_ind = alphabet.index(char)
        new_char = alphabet[(char_ind + key) % 26]
        encrypted += new_char
    
    return encrypted

def decrypt(strToEcnrypt,key):
    encrypted = ""

    for char in strToEcnrypt:
        char_ind = alphabet.index(char)
        
        new_char = alphabet[(char_ind - key) % 26]
        encrypted += new_char
    
    return encrypted

for i in range(0,26):
    print(f"Key ->  {i} , result -> " + decrypt("vppanlwxlyopyncjae",i))
