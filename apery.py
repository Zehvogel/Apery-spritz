#/usr/bin/python3

import secrets
import math


MAX_RND = 1000
N = 10000000


def gcd(a, b, c):
    d = math.gcd(a,b)
    if d == 1:
        return 1
    else:
        return math.gcd(d,c)

def tuple_gcd(t):
    a, b, c = t
    return gcd(a, b, c)

def get_three_rnds():
    a = secrets.randbelow(MAX_RND)
    b = secrets.randbelow(MAX_RND)
    c = secrets.randbelow(MAX_RND)
    return (a, b, c)

def get_rnd_list(length):
    rnd_list = []
    for i in range(length):
        rnd_list.append(get_three_rnds())
    return rnd_list

def main():
    coprimes = 0
    rnd_list = get_rnd_list(N)
    for i in rnd_list:
        if tuple_gcd(i) == 1:
            coprimes += 1
    print("N: {}\n", N)
    print("Number of coprimes: {}\n", coprimes)
    print("Approximation of Apery's constant: {}\n", N/coprimes)
main()
