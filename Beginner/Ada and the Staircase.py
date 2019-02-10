t = int(raw_input())
for i in xrange(t):
	n, k = map(int, raw_input().split())
	numArr =[]
	numArr = map(int, raw_input(). split())
	# print num
	prev=0
	ans = 0
	for num in numArr:
		# print("num is ", num, " prev is ", prev)
		if(num==prev):
			prev=num
			continue
		diff = num-prev
		req = diff//k
		if(req*k==diff):
			req-=1
		# print(req, "required to jump to ", num)
		ans+=req
		prev=num
	print ans