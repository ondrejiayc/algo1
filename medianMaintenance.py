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
	with open('Median.txt','r') as f:
		for i in range(2):
			n=int(f.readline())
			heappush(hmax,n)
			tot=tot+hmax[0]
		
		heappush(hmin,-heappop(hmax))
			
		for line in f:
			n=int(line)
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
			tot=(tot-hmin[0])%10000
	
	print 'Tot: '+str(tot)

if __name__=='__main__':
	main()
