t = int(raw_input())
for i in xrange(t):
	got = raw_input().split()
	n=int(got[0])
	p1=got[1]
	p2=""
	if(p1=="Dee"):
		p2="Dum"
	else:
		p2="Dee"
	dee0=0
	dum1=0
	# for j in xrange(n):
	# 	st = raw_input()
	# 	prev=''
	# 	for s in st:
	# 		if(prev==''):
	# 			if(s=='0'):
	# 				dee0+=1
	# 			elif(s=='1'):
	# 				dum1+=1
	# 		else:
	# 			if s==prev:
	# 				pass
	# 			else:
	# 				if(s=='0'):
	# 					dee0+=1
	# 				elif(s=='1'):
	# 					dum1+=1
	# 		# print("curr is ", s, " prev is ", prev)
	# 		prev=s
	# 	# print("dee0 is ", dee0, " dum1 is ", dum1)

	for j in xrange(n):
		st=raw_input()
		if st[0]==st[-1]:
			if st[0]=='0':
				dee0+=1
			else:
				dum1+=1
	
	if(dee0<dum1):
		print("Dee")
	elif(dee0>dum1):
		print("Dum")
	else:
		print(p1)
	