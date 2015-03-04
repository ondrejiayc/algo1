#!/usr/bin/python

from heapq import *

def main():
	tot=0
	#heap for larger half, add normal numbers
	hmax=[]
	#hepa for smaller half, add negative values
	hmin=[]
	# which heap is due for an insertion, true for min, false for max
	mainSwitch=True
	with open(file,'r') as f:
		for line in f:
			n=int(line.strip())			
			#decide which heap to add to
			if n>hmax[0]:
				heappush(hmax,n)
				if mainSwitch:
					heappush(hmin,-heappop(hmax))
			else:
				heappush(hmin,-n)
				if not mainSwitch:
					heappush(hmax,-heappop(hmin))
			mainSwitch=not mainSwitch
			#get median
			if mainSwitch:
			    med=hmax[0]
			else:
			    med=-hmin[0]
			#get tot
			tot=(tot+med)%10000
	
	print 'Tot: '+str(tot)

if __name__='__main__':
	main()
