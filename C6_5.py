def asteroid_collision(asts, n):

    index = len(asts)-1

    if asts == []:
        return asts

    elif n == 0 and asts[0] < 0:
        return asteroid_collision(asts, n+1)

    elif index == n and asts[n] > 0 :
        return asts

    elif index == n and asts[n] < 0 and asts[n-1] < 0:
        return asts

    elif len(asts)-1 <= n:
        return asts

    elif asts[n] > 0:
        a, b = asts[n], asts[n+1]

        if b > 0:
            return asteroid_collision(asts, n+1)
        else :
            b = b*-1

            if a == b:
                asts.pop(n)
                asts.pop(n)

            elif a > b:
                asts.pop(n+1)

            else :
                asts.pop(n)

            return asteroid_collision(asts, n-1)   

    elif asts[n] < 0:
        a, b = asts[n], asts[n-1]

        if b < 0:
            return asteroid_collision(asts, n+1)
    else:
        return asteroid_collision(asts, n+1)

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x, 0))