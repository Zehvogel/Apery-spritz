#/usr/bin/python3

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

def get_rnd_list(length, max_rnd):
    rnd_list = []
    for i in range(length):
        rnd_list.append(get_three_rnds(max_rnd))
    return rnd_list

def main():
    args = get_arguments()
    coprimes = 0
    N = args.N
    M = args.M
    time1 = time.time()
    rnd_list = get_rnd_list(N, M)
    time2 = time.time()
    rnd_gen_time = time2 - time1
    print(("[+] {0} Tripletts of random numbers created in {1}"
          +"seconds").format(N, rnd_gen_time))
    for i in rnd_list:
        if tuple_gcd(i) == 1:
            coprimes += 1
    time3 = time.time()
    print("[+] calculation time: {} seconds".format(time3 - time2))
    print("N: {}".format(N))
    print("Number of coprimes: {}".format(coprimes))
    print("Approximation of Apery's constant: {}".format(N/coprimes))
main()
