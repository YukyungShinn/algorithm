h,m=map(int,input().split())
if h==0 and m>=45:
    print(h, m-45)
elif h==0 and m<=44:
    print(h+23, m+15)
else:
    if 45<=m<=59:
        print(h, m-45)
    elif 0<=m<=44:
        print(h-1, m+15)
