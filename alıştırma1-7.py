n = 0
for i in range (100,1000):
    if int(str(i)[0]) + int(str(i)[1]) == int(str(i)[2]):
        n=n+1
        print(i)


print("koşulu sağlayan sayı adedi =",n)
