(m,n,k) = map(int, input().split())
row=0
column= 0
if n%k ==0:
    row= n//k
else:
    row= n//k +1
        
if m%k==0:
    column=m//k
else:
    column=m//k +1
print(column*row)
