def print1ToN(n) :
    if n > 1 :
        print1ToN(n-1)
        print(n , end = " ")
    elif n == 0 :
        print("1" , end = " ")
    else :
        print("1" , end = " ")

def printNto1(n) :
    if n > 1 :
        print(n , end = " ")
        printNto1(n-1)
    elif n == 0 :
        print("1" , end = " ")
    else :
        print("1" , end = " ")

n = int(input("Enter Input : "))
print1ToN(n)
printNto1(n)