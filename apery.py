#/usr/bin/python3

# Copyright © 2017 Leonhard Reichenbach
# This file is released under the MIT license.

import argparse
import sys
import random
import math
import time


#MAX_RND = 1000
#N = 10000000


def get_arguments():
    parser = argparse.ArgumentParser(description="A small program to"
                                     +"calculate Apéry's constant using" 
                                     +"(pseudo) random numbers.")
    parser.add_argument('-N', default=1000, help="The amount of random"
                        +"Numbers used. Defaults to 1000.", type=int)
    parser.add_argument('-M', default=1000, help="The maximum size any"
                        +"random number can take. Defaults to 1000", type=int)
    args = parser.parse_args()
    return args

def gcd(a, b, c):
    d = math.gcd(a,b)
    if d == 1:
        return 1
    else:
        return math.gcd(d,c)

def tuple_gcd(t):
    a, b, c = t
    return gcd(a, b, c)

def get_three_rnds(max_rnd):
    a = random.randint(0, max_rnd)
    b = random.randint(0, max_rnd)
    c = random.randint(0, max_rnd)
    return (a, b, c)

def main():
    args = get_arguments()
    coprimes = 0
    N = args.N
    M = args.M
    time1 = time.time()
    for i in range(N):
        triplett = get_three_rnds(M)
        if tuple_gcd(triplett) == 1:
            coprimes += 1
    time2 = time.time()
    print("[+] time: {} seconds".format(time2 - time1))
    print("N: {}".format(N))
    print("Number of coprimes: {}".format(coprimes))
    print("Approximation of Apery's constant: {}".format(N/coprimes))
main()
