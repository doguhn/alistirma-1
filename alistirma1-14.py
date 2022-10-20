n = 0
k = 121211
for x in range(1,121212):
    for y in range(1,121212):
        if x * y == 121212:
            n = x - y
            if n >= 0 and n <= k:
                k = n
                print(x,y)
