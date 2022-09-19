def isPalindrome(a,an,b):
    b+=a[an]  
    if an != 0:
        return isPalindrome(a,an-1,b)
    else:
        if a==b:
            print("'"+inp+"' is palindrome") 
        else:
            print("'"+inp+"' is not palindrome")

inp = input("Enter Input : ")
isPalindrome(inp,len(inp)-1,"")