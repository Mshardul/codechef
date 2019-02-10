def GetRes(num):
	n=len(num)
	maxno = max(num)
	ind = num.index(maxno)
	if(ind==0 or ind==(n-1)):
		return 1
	return min((1+GetRes(num[:ind])), (1+GetRes(num[ind+1:])))


t = int(raw_input())
for i in xrange(t):
	n = int(raw_input())
	num = [int(i) for i in raw_input().split()]
	out = GetRes(num)
	print(out)
