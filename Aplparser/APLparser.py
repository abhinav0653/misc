#!/usr/bin/python
from pyparsing import *
import sys
"""
	Abhinav Agrawal
	2016pcp5430@mnit.ac.in

	A simple parser for Array programming languages(APL)
"""


#symbol table
class symboltable:
	def __init__(self):
		self.mydict= {'dummy':'1 2 3'}
		
	def lookup(self,val):
		return self.mydict[val]

	def insert(self,key,val):
		self.mydict[key]=val

#An instance of symbol table
s_table = symboltable()


	
def tointlist(instr):
	res = [int(i) for i in instr]
	return res



def computation(left,right,op):
		if op=='iota':
			for i in range(1,int(right)+1):
				print i," ",
			print ""
			return

		if op=='rho':
			t1 = tointlist(left)
			t2 = tointlist(right)
			if len(t1) !=2:
				print "dimensions to be displayed are improper"
				return
			for i in range(0,t1[0]):
				for j in range(0,t1[1]):
					idx=((i*(t1[1]))+j)
					mod= len(t2)
					print t2[idx%mod],
				print ""
			return

			

		if left[0].isalpha():
			
			if len(right) == 0:
				try:
					print tointlist(s_table.lookup(left))
				except :
					print "undefined value!!"
				return

			if op=='=':
				s_table.insert(left,right)
				return
			
 
			leftval = tointlist(s_table.lookup(left))

			if len(right) >1:
				print "Invalid argument on RHS of operator"
				return

			rightval=int(right[0])
			
			if op=='+':
				res = [(i+rightval) for i in leftval]
			elif op=='-':
				res = [(i-rightval) for i in leftval]
			else:
				res = [(i*rightval) for i in leftval]

		else:

			t1 = tointlist(left)
			t2 = tointlist(right)
			if len(t1) != len(t2):
				print "error in input"
				return	
			
			rg=len(t1)
			if op=='+':
				res = [(t1[i]+t2[i]) for i in range(0,rg)]
			elif op=='-':
				res = [(t1[i]-t2[i]) for i in range(0,rg)]
			else:
				res = [(t1[i]*t2[i]) for i in range(0,rg)]
		print res
			


#Operation parser
Opparser= Forward()
op = oneOf('= + - * rho iota').setResultsName("operator")
p1 = Word(alphas).setResultsName("left") + op + OneOrMore(Word(nums)).setResultsName("right")
p2 = OneOrMore(Word(nums)).setResultsName("left") + op + OneOrMore(Word(nums)).setResultsName("right")
p3 = op + Word(nums).setResultsName("right")
p4 = Word(alphas).setResultsName("left")
Opparser << ( p1 | p2 | p3 | p4)


def test(strg):
	try:
		result= Opparser.parseString(strg)	
		computation(result.left,result.right,result.operator)
	except ParseException, err:
		print " "*err.loc + "^\n" + err.msg
        	print err
#Main
query=sys.stdin.readline()
while 1:
	test(query)
	query=sys.stdin.readline()





