from random import randint, randrange, shuffle

class big_prime_generator:
    def __init__(self, n):
        self.n = n
        self.small_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
                            71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
                            151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
                            233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
                            317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
                            419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
                            503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
                            607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                            701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
                            811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
                            911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    def generate_simple_prediction(self):
        target = 2 ** self.n
        prime_candidate = []
        for i in range(target - 2 ** 15, target + 2 ** 15):
            if self.check_if_divisible_by_small_prime(i):
                prime_candidate.append(i)

        shuffle(prime_candidate)

        return prime_candidate

    def check_if_divisible_by_small_prime(self, n):
        for i in self.small_prime:
            if n % i == 0:
                return False
        return True

    def Miller_Rabin_test(self, k, n):
        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s >>= 1
        for _ in range(k):
            a = randrange(2, n - 1)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True


    def generate(self):
        prime_candidate = self.generate_simple_prediction()
        for i in prime_candidate:
            if self.Miller_Rabin_test(100, i):
                return i

        return -1


def main():
    # Generate a big prime of about 50 bits
    n = 50
    bpg = big_prime_generator(n)
    big_prime = bpg.generate()
    print(big_prime)

if __name__ == "__main__":
    main()
