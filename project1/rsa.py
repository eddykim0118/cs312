import random
import sys

# This may come in handy...
from fermat import miller_rabin

# If you use a recursive implementation of `mod_exp` or extended-euclid,
# you recurse once for every bit in the number.
# If your number is more than 1000 bits, you'll exceed python's recursion limit.
# Here we raise the limit so the tests can run without any issue.
# Can you implement `mod_exp` and extended-euclid without recursion?
sys.setrecursionlimit(4000)

# When trying to find a relatively prime e for (p-1) * (q-1)
# use this list of 25 primes
# If none of these work, throw an exception (and let the instructors know!)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


# Implement this function
def ext_euclid(a: int, b: int) -> tuple[int, int, int]:
    """
    The Extended Euclid algorithm
    Returns x, y , d such that:
    - d = GCD(a, b)
    - ax + by = d

    Note: a must be greater than b
    """
    if b > a:
        raise ValueError("a must be greater than b")
    
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_s, old_t, old_r


# Implement this function
def generate_large_prime(bits=512) -> int:
    """
    Generate a random prime number with the specified bit length.
    Use random.getrandbits(bits) to generate a random number of the
     specified bit length.
    """
    while True:
        n = random.getrandbits(bits)

        n |= (1 << bits - 1) | 1

        if miller_rabin(n, 20) == "prime":
            return n


# Implement this function
def generate_key_pairs(bits: int) -> tuple[int, int, int]:
    """
    Generate RSA public and private key pairs.
    Return N, e, d
    - N must be the product of two random prime numbers p and q
    - e and d must be multiplicative inverses mod (p-1)(q-1)
    """
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)

    while p == q:
        q = generate_large_prime(bits) 

    N = p * q
    totient = (p - 1) * (q - 1)

    for e in primes:
        if totient > e:
            x, y, d = ext_euclid(totient, e)
        else:
            y, x, d = ext_euclid(e, totient)

        if d == 1:
            break

    else:
        raise ValueError("No valid e found")
    
    if totient > e:
        d = y % totient
    else:
        d = x % totient

    if d < 0:
        d += totient

    return N, e, d
