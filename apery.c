/* Author:
 *  Leonhard Reichenbach
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>

#define FAILURE(progname, msg...) \
   fprintf(stderr,msg); usage(progname); exit(EXIT_FAILURE);

static void usage(const char *progname) {
  int indent = strlen(progname) + 8;
  fprintf(stderr, "Usage: %s %s\n%*s%s\n",
          progname, "<Number of random number tripletts used N>",
          indent, " ", "<Max random number size M>");
}

int gcd(int a, int b) {
  uint64_t temp;
  while (b != 0) {
    temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

int triple_gcd(int a, int b, int c) {
  uint64_t d = gcd(a, b);
  if (d != 1) {
    d = gcd(d, c);
  }
  return d;
}

int randbelow(uint64_t max_rnd) {
  return rand() % (max_rnd+1);
}

int main(int argc, char *argv[]) {
  uint64_t N, M;

  switch (argc) {
    case 1:
      N = 1000;
      M = 1000;
      break;
    case 3:
      if (sscanf(argv[1], "%lu", &N) * sscanf(argv[2], "%lu", &M) != 1) {
        FAILURE(argv[0], "%s","");
      }
      break;
    default:
      FAILURE(argv[0], "%s\n","Illegal parameter count!");
  }

  srand(3);

  uint64_t coprimes = 0;

  for (uint64_t i = 0; i < N; i++) {
    uint64_t a = randbelow(M);
    uint64_t b = randbelow(M);
    uint64_t c = randbelow(M);
    if (triple_gcd(a, b, c) == 1) {
      coprimes++;
    }
  }
  
  printf("N: %lu\n", N);
  printf("Number of coprimes: %lu\n", coprimes);
  printf("Approximation of Apery's constant: %lf\n", (N/((double) coprimes)));

  return EXIT_SUCCESS;
}
