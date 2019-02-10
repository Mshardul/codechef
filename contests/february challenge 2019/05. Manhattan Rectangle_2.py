def query(x, y):
	q="Q "+str(x)+" "+str(y)+"\n"
	inp=int(raw_input(q))
	return inp

t=int(raw_input())
while t>0:

	n=1000000000

	bx=0
	by=0
	inp=query(bx, by)
	if(inp!=0):
		if(inp>n):
			bx=n
			by=inp-n
		else:
			bx=inp
		inp=query(bx, by)
		if(inp!=0):
			bx=bx-(inp/2)
			by=inp/2
			inp=query(bx, by)

	tx=n
	ty=n
	inp=query(tx, ty)
	if(inp!=0):
		if(inp>n):
			tx=0
			ty=(2*n)-inp
		else:
			tx=n-inp
		inp=query(tx, ty)
		if(inp!=0):
			tx=(inp/2)
			ty=ty-(inp/2)
			inp=query(tx, ty)

	q="A "+str(bx)+" "+str(by)+" "+str(tx)+" "+str(ty)
	print(q)
	inp=int(raw_input())

	t-=1