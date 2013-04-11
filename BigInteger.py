def add(num1,num2):
	lenA=len(num1)
	lenB=len(num2)
	s=''
	carr=0
	if lenA<lenB:
		num1=('0'*(lenB-lenA))+num1
		lenA=lenA+(lenB-lenA)
	if lenB<lenA:
		num2=('0'*(lenA-lenB))+num2
		lenB=lenB+(lenA-lenB)
	c=lenA-1
	while c>=0:
		sum=int(num1[c])+int(num2[c])
		sum=sum+carr
		r=sum%10
		if c==0:
			s=`sum`+s
			return(s)
		else:
			
			s=`r`+s
		carr=sum/10
		c=c-1
		
def product(num1, num2):
	carr=0
	if len(num2)>len(num1):
		temp=num2
		num2=num1
		num1=temp
		
	lenA=len(num1)
	lenB=len(num2)
	s=''
	sum=0
	carr=0
	c=lenA-1
	d=lenB-1
	p=list(' '*lenB)
	while d>=0:
		c=lenA-1
		carr=0
		while c>=0: 
			pro=int(num1[c])*int(num2[d])
			pro=pro+carr
			r=pro%10
			if c==0 :
				p[d]=`pro`+p[d]
			else :
				p[d]=`r`+p[d]
			c=c-1	
			carr=pro/10
		d=d-1
	new_p = [x[:-1] for x in p]
	new_p.reverse()
	for i in range(len(new_p)):
		new_p[i]=new_p[i]+('0'*i)

	new_p.reverse()
	l=len(new_p)
	l=l-1
	for i in range(l):
		temp=add(new_p[i],new_p[i+1])
		new_p[i+1]=temp
	return temp
				
			
			
			
		
		
	
