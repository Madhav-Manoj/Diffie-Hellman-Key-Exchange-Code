import random

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime():
    return random.choice([num for num in range(10, 1001) if is_prime(num)])

def calculate_primitive_root(p):
    g = random.randint(2, p - 1)
    return g

def generate_private_key():
    return random.randint(2, 100)

def calculate_public_key(privateKey, g, p):
    return (g ** privateKey) % p

def calculate_shared_secret(privateKey, gotPublicKey, p):
    return (gotPublicKey ** privateKey) % p

def print_step(step, aPrivateKey, aPublicKey, bobPrivateKey, bPublicKey, TheSecret):
    print(f"current step: {step}:")
    print(f"Alice's Private Key={aPrivateKey}, Public Key={aPublicKey}")
    print(f"Bob's Private Key = {bobPrivateKey}, Public Key={bPublicKey}")
    print(f"Shared Secret={TheSecret}")
    print("")
p = generate_prime()
print(f"random prime number (p): {p}")
g = calculate_primitive_root(p)
print(f" Root (g) modulus p: {g}")
a = generate_private_key()
b = generate_private_key()
A = calculate_public_key(a, g, p)
B = calculate_public_key(b, g, p)
ssA = calculate_shared_secret(a, B, p)
ssB = calculate_shared_secret(b, A, p)
print_step(1, a, A, b, B, ssA)
print_step(2, b, B, a, A, ssB)