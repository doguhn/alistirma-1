n = 1

for i in range(1,351):
    k = 125 % i
    l = 200 % i
    m = 350 % i
    if k==l==m and i>n:
        n = i

    

print ("En büyük kalanı veren x sayısı =",n)
