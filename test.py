space = 7
star = 0

for i in range(space, 0, -1):
    print("="*i + "= " + " *"*star + "="*i)
    # print(" "*i + "="*star*2)
    star = space - i