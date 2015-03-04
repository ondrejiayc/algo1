#!/usr/bin/python

def main():
    d={}
    with open('algo1-programming_prob-2sum.txt','r') as f:
        for line in f:
            n=long(line.strip())
            if n not in d:
                d[n]=True
    
    print 'Array read in...'
    print ''
    
    total=0
    for i in range(-10000,10001):
        print 'Testing '+str(i)
        for n in d:
            if ((i-n) in d) and (n!=(i-n)):
               total+=1
               print total
               break
    
    print total

if __name__=='__main__':
    main()