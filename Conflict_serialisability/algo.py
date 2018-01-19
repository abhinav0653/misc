#!/usr/bin/python
from pyparsing import *
import sys
file = open(sys.argv[1],"r")
lines = file.readlines()
nlines = len(lines)
n_trans= int(lines[0])
V=n_trans
MAX=1000
G = [[0]*(V+1) for x in xrange(0,(V+1))]
global list
list=[]


tranStmt = Forward() 
Transaction = "T" + Word(nums).setResultsName("TransID") + ":" 
readident = Keyword('read',caseless=True) 
writeident = Keyword('write',caseless=True) 
readt = readident + "(" + Word(alphas).setResultsName("rditem") + ")" 
writet = writeident + "(" + Word(alphas).setResultsName("writem") + ")" 
transCondition = Transaction + ((readt) | (writet)) 
tranStmt << transCondition.setResultsName("transToken") 


def mark(u,v):
	G[u][v]=1

def DFS(i,color):
	color[i]=1
	for j in range(1,(V+1)):
		if G[i][j]!=0:
			if color[j]==0:
				if (DFS(j,color)):
					return True
			elif color[j]==1:
				print "Graph has cycle"
				return True
			else:
				continue
		else:
			continue
	color[i]=2
	global list
	list += [i]
	return False


def hasCycle(G):
	color = [0]*(V+1)
	for v in range(1,V+1):
		if color[v]==0: 
			if(DFS(v,color)):
				return True
	return False


def conflictop(op1,op2):
	if( op1 | op2 ):
		return True
	else:
		return False
		
#Construction of Adjacenty matrix for Graph
for i in range(1,nlines):
	wrapper = tranStmt.parseString(lines[i])
	TID1 = int(wrapper.TransID)
	if wrapper.rditem:
		optype1=0
		data1=wrapper.rditem
	elif wrapper.writem:
		optype1=1
		data1=wrapper.writem
	else:
		optype1=2
#	TID1,optype,data

	for j in range(i+1,nlines):
		wrapper = tranStmt.parseString(lines[j])
		TID2 = int(wrapper.TransID)
		if wrapper.rditem:
			optype2=0
			data2=wrapper.rditem
		elif wrapper.writem:
			optype2=1
			data2=wrapper.writem
		else:
			optype2=2
#		TID2,optype,data
		if TID1!=TID2 and data1==data2 and conflictop(optype1,optype2):
			mark(TID1,TID2)

print "Adjaceny Matrix for Graph is:"
for i in range (1,V+1):
		print G[i][1:]
#Determination of cycle if it exists or else a serialisability order
if(hasCycle(G)):
	print("Graph has cycle and thus not confict serialisable")
else:
	print("Topological sorted order is as shown:")
	list.reverse()
	print list
	
	
