t=int(raw_input())
while t>0:

	n=100

	bx=0
	by=0
	q="Q "+str(bx)+" "+str(by)
	print(q)
	inp=int(raw_input())
	if(inp!=0):
		if(inp>n):
			by=n
			bx=inp-n
		by=inp
		q="Q "+str(bx)+" "+str(by)
		print(q)
		inp=int(raw_input())
		if(inp!=0):
			bx=by-(inp/2)
			by=inp/2
			q="Q "+str(bx)+" "+str(by)
			print(q)
			inp=int(raw_input())

	tx=n
	ty=n
	q="Q "+str(tx)+" "+str(ty)
	print(q)
	inp=int(raw_input())
	if(inp!=0):
		tx=tx-inp
		q="Q "+str(tx)+" "+str(ty)
		print(q)
		inp=int(raw_input())
		if(inp!=0):
			ty=tx+(inp/2)
			tx=tx-(inp/2)
			q="Q "+str(tx)+" "+str(ty)
			print(q)
			inp=int(raw_input())

	q="A "+bx+" "+by+" "+tx+" "+ty
	print(q)
	inp=int(raw_input())

	t-=1