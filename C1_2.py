a = input('Enter your High and Weight : ')     
n = a.split()

height = float(n[0])
weight = float(n[1])

c = weight/(height**2)
if c<18.5:
    print('Less Weight')
elif c>=18.5 and c<23:
    print('Normal Weight')
elif c>=23 and c<25:
    print('More than Normal Weight')
elif c>=25 and c<30:
    print('Getting Fat')
elif c>=30:
    print('Fat')