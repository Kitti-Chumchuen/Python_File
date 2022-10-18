def pantip(k, n, arr, path, i):

    if arr[i[0]] == k:
        if i[0] == k:
            return n
        else:
            print(arr[i[0]])
            i[0] += 1
            i[4]  = i[0]
            n += 1
            return pantip(k, n, arr, path, i)
    
    elif arr[i[1]+1] == None:
        i[0] += 1
        i[1]  = 0

    elif arr[i[4]+1] == None:
        i[1] += 1
        i[4]  = i[0]

    elif i[2] == k:
        print(path)
        if i[3] != 0:
            print(path)
            i[3] = 0
        path.clear()
        i[2] = 0
        i[4] = i[0]
        n += 1
        return pantip(k, n, arr, path, i)

    elif i[0] == arr[-1]:
        return n

    elif arr[i[4]] < k and i[3] != 0:

        if arr[i[4]+1] == arr[i[4]]:
            path.append(arr[i[4]+1])
            i[2] += arr[i[4]+1]
            i[1] = i[4]+1
            i[4] += 2
        else:
            path.append(arr[i[4]])
            i[2] += arr[i[4]]
            i[4] += 1
        
        return pantip(k, n, arr, path, i)

    elif arr[i[4]] < k and i[3] == 0:       # i[0] : n ที่กำลังเช็ค
        if arr[i[4]] == arr[i[4]-1]:        # i[1] : Updateตำแหน่ง!
            i[3] += 1
        path.append(arr[i[4]])              # i[2] : ผลรวมของ n ใน path
        i[2] += arr[i[4]]
        i[4] += 1                           # i[3] : ถ้ามีเลขซ้ำกัน
        return pantip(k, n, arr, path, i)   # i[4] : Updateจนหมดแล้วreset
     
    elif arr[i[1]] > k:
        i[1] += 1
        return pantip(k, n, arr, path, i)
    
    else:
        return n
    

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [], [0,0,0,0,0])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))