import random
import math

def is_prime (number):
    if number < 2:
        return False
    for i in range (2, number // 2 +1):
        if number % i == 0:
            return False
    return True

def generate_prime(min, max):
    prime = random.randint(min, max)
    while not is_prime(prime):
        prime = random.randint(min, max)
    return prime

def mod_inverse(public_key, phi):
    for d in range (3, phi):
        if (d * public_key) % phi == 1:
            return d 
        
def generate_unique_primes():
    p, q = generate_prime(1000,50000), generate_prime(1000,50000)
    while p == q:
        q = generate_prime(1000,50000)
    return p,q
        
def generate_keys(p,q):
    #
    phi_n = (p-1) * (q-1)
    #
    public_key = random.randint (3, phi_n-1)
    while math.gcd(public_key, phi_n) != 1:
        public_key = random.randint (3, phi_n - 1)
    #
    private_key = mod_inverse(public_key, phi_n)

    return public_key,private_key

def encrypt(strToEncode,public_key,n):
    strToEncode = [ord(ch) for ch in strToEncode]
    ecnryptedMessage = [pow(ch, public_key, n) for ch in strToEncode]

    return ecnryptedMessage
        
def decrypt(strToDecrypt,private_key,n):
    decryptedMessage= [pow(ch, private_key, n) for ch in strToDecrypt] 
    decryptedMessage = "".join(chr(ch) for ch in decryptedMessage)

    return decryptedMessage


message = "100"

p,q = generate_unique_primes()
public_key,private_key = generate_keys(p,q)
print ("Публічний ключ -> ", public_key)
print ("Приватний ключ -> ", private_key)

n = p * q

encrypted = encrypt(message,public_key,n)
print ("Зашифровано ->", encrypted)


decrypted = decrypt(encrypted,private_key,n)
print(("Розшифровано -> " + decrypted))

if (message == decrypted):
    print("Результат розшифрування правильний")
else :
    print("Результат розшифрування не правильний")
