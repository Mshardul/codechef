def gcd(a, b):
	if(b==0):
		return a
	return gcd(b, a%b)

t=int(raw_input())
while(t>0):
	n, a, b, k = map(int, raw_input().split())
	x=n/a
	y=n/b
	z=(n*gcd(a,b))/(a*b)
	# print(x, y, z)
	if(x+y-(2*z))>=k:
		print("Win")
	else:
		print("Lose")
	t-=1