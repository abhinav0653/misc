all: basic.prep basic.cp basic.o basic.out
	
basic.prep: basic.c
	gcc -E basic.c -o basic.prep

basic.cp: basic.c
	gcc -S basic.c -o basic.cp

basic.o: basic.c
	gcc -c basic.c -o basic.o

basic.out: basic.o
	gcc basic.o -o basic.out

clean:
	rm -rf basic.prep basic.cp basic.o basic.out
