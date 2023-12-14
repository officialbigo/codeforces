T=int(input())
for t in range(T):
    n=int(input())
    is_cat=input()
    x=0
    m=0
    e=0
    o=0
    ans="NO"
    flag=0
    for i in is_cat:
        if i in ("m","M") and m==0:
            x=1
            continue
        elif i in ("e","E") and e==0 and x==1:
            m=1
            continue
        elif i in ("o","O") and o==0 and m==1:
            e=1
            continue
        elif i in ("w","W") and e==1:
            o=1
            continue
        else:
            flag=1
            break
    if m+e+o+x==4 and flag==0:
        ans="YES"
    print(ans)
