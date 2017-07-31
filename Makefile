.PHONY: all clean

CC=gcc
CFLAGS=-Wall -Werror -O3 -march=native

all: apery.x

%.x:%.c
	${CC} ${CFLAGS} -o $@ $<

clean:
	rm -f apery.x
