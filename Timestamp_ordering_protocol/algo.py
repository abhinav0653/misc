#!/usr/bin/python

"""
	Abhinav Agrawal
	2016pcp5430@mnit.ac.in
"""


from pyparsing import *
import sys

logical_counter=1
def writelogfile(str):
	log_file.writelines(str+"\n")
	return

	
def initiateRollback(TransID):
	print "rolling back"
	Blacklist[TransID]=True
	writelogfile("T"+str(TransID)+ " rolled back and will be restarted with new timestamp")
	return

def cascaderollbackU(TransID,dirty_read):
	initiateRollback(TransID)
	for j in range(1,n_trans+1):
		if dirty_read[TransID][j]==1:
			cascaderollbackU(j,dirty_read)


def cascaderollback(num):
	print "entered cascaderollback"
	dirty_read=[[0]*(n_trans+1) for x in xrange(0,n_trans+1)]
	for i in range(1,num):
		wrapper1 = tranStmt.parseString(lines[i])
		TransID1 = int(wrapper1.TransID)
		item1 = wrapper1.writem
		if item1:
			for j in range(i+1,num):
				wrapper2 = tranStmt.parseString(lines[j])
				TransID2 = int(wrapper2.TransID)
				item2 = wrapper2.rditem
				if item2:
					if TransID1!=TransID2 and item1==item2:
						dirty_read[TransID1][TransID2]=1

	TransID = int(tranStmt.parseString(lines[num]).TransID)
	cascaderollbackU(TransID,dirty_read)
		

data_wmap= {}
data_rmap={}
val = {}
TS = []
Blacklist = {}

def condition(item,id,rflag):
#read stamp for write if rflag is 1 and similar
	w_stamp = data_wmap[item]
	r_stamp = data_rmap[item]

	if rflag:	
		if TS[id] < w_stamp:
			return False
		else:
			return True
	else:
		if (TS[id] < r_stamp) or (TS[id] < w_stamp):
			return False
		else:
			return True

def max(a,b):
	if a>b:
		return a
	else:
		return b


def updateDataStamp(item,TransID,rflag):
	if rflag:
		data_rmap[item]=max(TS[TransID],data_rmap[item])
		if data_rmap[item] == TS[TransID]:
			writelogfile("Read timestamp of " + item + " updated to " + str(data_rmap[item]) + " by transaction " + str(TransID))
		else:
			writelogfile("Read timestamp of " + item + " retained to " + str(data_rmap[item])+ " by transaction " + str(TransID))		
	else:
		data_wmap[item]=TS[TransID]
		writelogfile("Write timestamp of " + item + " updated to " + str(data_wmap[item]) + " by transaction " + str(TransID))



def updateDataItem(item,newval,rflag):
	if rflag == False:
		val[item]=newval


def test(str):
	print str,
	writelogfile(str[:-1])
	try:
		pOut = tranStmt.parseString(str)
		TransID=int(pOut.TransID)
#assign a timestamp
		if assigned[TransID]==False:
			global logical_counter
			TS[TransID]=logical_counter
			assigned[TransID]=True
 			logical_counter=logical_counter+1

		if Blacklist[TransID]:
			writelogfile("Instruction not executed!!")
			writelogfile("Transaction with TransID " + pOut.TransID + " is already rolled back")
			return

		rditem=pOut.rditem
		writem=pOut.writem
		rflag=False
		item = writem
		if len(item) == 0:
			rflag=True
			item=rditem
	
		if item in val:
			""
		else:
			val[item]=10	
		if item in data_wmap:
			data_wmap[item]
		else:
			data_wmap[item]=0
		if item in data_rmap:
			data_rmap[item]
		else:
			data_rmap[item]=0
	
		if condition(item,TransID,rflag):
			updateDataStamp(item,TransID,rflag)
		else:
			return -1	
	except ParseException, err:
		print err


#Parser for input
tranStmt = Forward()
Transaction = "T" + Word(nums).setResultsName("TransID") + ":"
readident = Keyword('read',caseless=True)
writeident = Keyword('write',caseless=True)
readt = readident + "(" + Word(alphas).setResultsName("rditem") + ")"
writet = writeident + "(" + Word(alphas).setResultsName("writem") + ")"
transCondition = Transaction + ((readt)|(writet))
tranStmt << transCondition.setResultsName("transToken")


#main
i_file = open(sys.argv[1],"r")
log_file = open("log.txt","w")
lines = i_file.readlines()
n_trans = int(lines[0])
assigned = [False for x in range(0,n_trans+1)]
TS = [x for x in range(0,n_trans+1)]

for i in range(1,n_trans+1):
	Blacklist[i]=False
for i in range(1,len(lines)):	
	ret=test(lines[i])
	if(ret == -1):
		cascaderollback(i)

writelogfile("")
str_ts = " ".join(str(TS[1:n_trans+1]))
writelogfile("Additional information:")			
writelogfile("Timestamps of transactions starting from index 1 to end are:")
writelogfile(str_ts)
log_file.close()
log_file = open("log.txt","r")
print "\n \n"
print "**************Printing log file*************"
for i in log_file.readlines():
	print i,
