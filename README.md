# Learn Vanilla RSA

This is a simple project implemented in `Python` to learn how the RSA algorithm works.

## Basic Procedure
1. Generate two prime numbers `p` and `q`
   + To approach this goal, we first need to code a large prime generator.
   + First, we need to pin down the number of bits we need (for example 128 bits).
   + Then, we search through a range of numbers around $2^{128}$ that are **not divisible by primes less than 1000 ** (This can be done easily by googling prime numbers less than 1000). These numbers are called candidates. This step largely shrinks the range of possible candidates, thereby speeding up the algorithm.
   + We shuffle the candidates to introduce randomness.
   + Finally, we use [Miller-Rabin Test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_test) to see if the numbers in the candidate list are prime or not. Once we find a possible prime, we return it.
2. Generate `e` and `d`
   + After generating `p` and `q`, we can get $\phi_N=(p-1)(q-1)$, and $N=pq$.
   + Then, we try to find `e` and `d` such that $ed = 1\text{ mod } \phi_N$.
3. Choose the message `m` to be encrypted, and we are ready for RSA.
   +  Encryption: $c=m^e\text{ mod }N$, where $c$ is the ciphertext.
   +  Decryption: $m=c^d\text{ mod }N$.

## A Word of Warning
This project is not a cryptanalysis, it is just a learning project. It is served to show how the RSA algorithm works in its simplest vanilla form. The real RSA is much more complex than this and introduces more security.

Also, RSA algorithm is a deterministic encryption algorithm, thereby not CPA-secure. To learn more about CPA-secure version of RSA, check out [OAEP](https://en.wikipedia.org/wiki/Optimal_asymmetric_encryption_padding).
