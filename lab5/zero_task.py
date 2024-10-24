def encrypt(strToEcnrypt,key):
    answers = []

    for i in range(0,key):
        answers.append(strToEcnrypt[i::key])

    answers = answers[::-1]
    result = ''.join(answers)

    return result

def decrypt(encryptedText, key):
    part_size = len(encryptedText) // key
    extra = len(encryptedText) % key

    parts = []
    start = 0
    for i in range(key):
        size = part_size + 1 if i < extra else part_size
        parts.append(encryptedText[start:start + size])
        start += size

    parts = parts[::-1]

    result = []
    for i in range(part_size + 1):
        for part in parts:
            if i < len(part):
                result.append(part[i])

    return ''.join(result)
        


phraseToEncrypt = "криптографія"
encrypted = encrypt(phraseToEncrypt,3)
print("Зашифровано -> " + encrypted)

decrypted = decrypt(encrypted,3)
print(("Розшифровано -> " + decrypted))

if (phraseToEncrypt == decrypted):
    print("Результат розшифрування правильний")
else :
    print("Результат розшифрування не правильний")





