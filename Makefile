# Copyright (c) 2017 Leonhard Reichenbach
# This file is released under the MIT license.
.PHONY: all clean

CC=gcc
CFLAGS=-Wall -Werror -O3 -march=native -fopenmp

all: apery.x

apery.x:pcg_basic.o apery.o
	${CC} -o $@ $^ ${CFLAGS}

clean:
	rm -f *.x *.o
