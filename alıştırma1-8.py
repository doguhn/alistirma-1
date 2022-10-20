n = 0
for i in range (100,1000,2):
    if str(i)[0]==(str(i)[1]) or str(i)[0]==str(i)[2] or str(i)[2]==str(i)[1]:
        n = n + 1
       

print(n)
