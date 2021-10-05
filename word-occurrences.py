s = list(input().split())
if len(s)==0:
	print("!!Blank Input!!")
else:
	wlist = {}
	for a in s:
		if wlist.get(a)==None:
			wlist[a]=1
		else:
			wlist[a]+=1
	for a in wlist:
		print(a,'=',wlist[a])
print()
