inp = input('Enter Input : ').split(",")
opt, num, n = "", [], 0
for i in inp:
    a = i.split(" ")
    opt += a[0]
    num[n] = a[1]
    n += 1
print(opt, num)