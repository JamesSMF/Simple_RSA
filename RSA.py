from generate_big_prime import big_prime_generator
from random import randrange
from math import sqrt

class RSA_instance:
    def __init__(self, N, e, d):
        self.N = N
        self.e = e
        self.d = d

    def encrypt(self, m):
        return pow(m, self.e, self.N)

    def decrypt(self, c):
        return pow(c, self.d, self.N)


def main():
    # Generate a big prime of about 50 bits
    n = 128
    bpg = big_prime_generator(n)
    p = bpg.generate()
    q = bpg.generate()
    N, phi_N = p * q, (p - 1) * (q - 1)

    # Calculate e and d
    e = randrange(2, int(sqrt(phi_N)))
    while True:
        try:
            d = pow(e, -1, phi_N)
            break
        except:
            e += 1

    rsa = RSA_instance(N, e, d)

    message = 114514
    cipher = rsa.encrypt(message)
    print(cipher)
    decrypted = rsa.decrypt(cipher)
    print(decrypted)

if __name__ == "__main__":
    main()
