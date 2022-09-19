def gcd(a,b):
    n, t = int(a), int(b)
    if a<0:
        a-= 0.001
        m = int(((a-n)*-1)*1000) 
    else:
        a+= 0.001
        m = int((a-n)*1000)
    #a = int("{:.4f}".format(a))
    #print("A =",a)
    if m==0:
        return gcd(a,b)
    if m<=n and m<=t and a>0 and b>0:
        if n%m==0 and t%m==0:
            b = int(b)
            b += a-n
        return gcd(a,b)
    elif m<=(n*-1) and m<=(t*-1) and a<0 and b<0:
        if n%m==0 and t%m==0:
            b = int(b)
            b += a-n
        return gcd(a,b)
    elif m<=n and m<=(t*-1) and a>0 and b<0:
        if n%m==0 and t%m==0:
            b = int(b)
            b += (a-n)*-1
        return gcd(a,b)
    elif m<=(n*-1) and m<=t and a<0 and b>0:
        if n%m==0 and t%m==0:
            b = int(b)
            b += (a-n)*-1
        return gcd(a,b)
    else:
        x,y = int(a),int(b)
        if a>0 or b>0:
            T = int((b-t)*1000)
        if b<0:
            T = int(((b-t)*-1)*1000)
        if x==0 and y==0:
            print("Error! must be not all zero.")
        elif x==0 and y>0:
            print("The gcd of",y,"and",x,"is :",y)
        elif x==0 and y<0:
            print("The gcd of",x,"and",y,"is :",y*-1)
        elif y==0 and x>0:
            print("The gcd of",x,"and",y,"is :",x)
        elif y==0 and x<0:
            print("The gcd of",y,"and",x,"is :",x*-1)
        else:
            if x>y:
                print("The gcd of",x,"and",y,"is :",T)
            else:
                print("The gcd of",y,"and",x,"is :",T)

# ---------- Program ---------- #
inp = input("Enter Input : ").split(" ")
gcd(int(inp[0]),int(inp[1]))