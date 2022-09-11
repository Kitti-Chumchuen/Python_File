from itertools import count

class translator:
    def deciToRoman(self, num):
        a=len(num)
        count=0
        b = []
        c=num
        for x in range(1,a):
            #b[count] = int(c%10)
            b.append(int(c%10))
            c=c/10
            count+=1
            print(b[count],sep=(' '))
        return count

    def romanToDeci(self, s):
        return 2

num = (input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))