t=int(raw_input())
while t>0:
	dic={}
	st=[]
	n=int(raw_input())
	for i in range(n):
		temp_lst=raw_input()
		st.append(temp_lst)
	dic={}
	for i in st[0]:
		if i not in dic:
			dic[i]=1
	for i in range(1, n):
		temp_dic={}
		for j in st[i]:
			if j in dic:
				temp_dic[j]=1
		for(k, v) in temp_dic.items():
			dic[k]+=1

	# for(k,v) in dic.items():
		# print("k: ", k, " v: ", v)

	ans=0
	for(k,v) in dic.items():
		if(v==n):
			ans+=1
	print(ans)
	t-=1