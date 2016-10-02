def instr(string,idx,start=0,n=1):
	if string.count(idx)<n:
		return -1
	if n==1:
		return string.find(idx,start)
	if n>1:
		loc=0
		for n in range(1,n+1):
			if n==1:
				loc=string.find(idx,start)
			else:
				loc=string.find(idx,loc+1)
		return loc
    
    
    
    
In [3]: instr('this function is like Oracle\'s instr','i',n=3)
Out[3]: 14
