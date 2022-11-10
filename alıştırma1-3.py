x = 1
e = 1 #0! = 1 olduğu için 1'den başladık.
for i in range (1,10000):
    x = i*x
    e = 1/x + e

print (e)


