def encrypt(plaintext, key):
    ciphertext = []
    key_length = len(key)
    
    for i, char in enumerate(plaintext):
        if 'а' <= char <= 'я':
            shift = ord(key[i % key_length]) - ord('а')
            encrypted_char = chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(char)
    
    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    plaintext = []
    key_length = len(key)
    
    for i, char in enumerate(ciphertext):
        if 'а' <= char <= 'я':
            shift = ord(key[i % key_length]) - ord('а')
            decrypted_char = chr((ord(char) - ord('а') - shift + 32) % 32 + ord('а'))
            plaintext.append(decrypted_char)
        else:
            plaintext.append(char)
    
    return ''.join(plaintext)


phraseToEncrypt = "криптографічнiметодизахистуінформації"
key = "жупанин"

encrypted = encrypt(phraseToEncrypt,key)
print("Зашифровано -> " + encrypted)

decrypted = decrypt(encrypted,key)
print(("Розшифровано -> " + decrypted))

if (phraseToEncrypt == decrypted):
    print("Результат розшифрування правильний")
else :
    print("Результат розшифрування не правильний")
