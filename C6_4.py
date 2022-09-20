def pantip(k, n, arr, path, i):
    if arr[0]==k:
        print(arr.pop(0))
        pantip(k, n, arr, path)
    if arr[0]<k:
        path[i] += 1

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [], 0)
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))