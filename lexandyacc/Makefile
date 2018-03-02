all:
	yacc -d calc.yacc
	lex calc.lex
	cc lex.yy.c y.tab.c -o calc.out
clean:
	rm -rf lex.yy.c y.tab.h y.tab.c calc.out
