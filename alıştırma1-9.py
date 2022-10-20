list = []
toplam = 0
for i in range(1,1000):
    if i < 9:
        print(i,end=" ")
    elif 10 <=i <= 99 and int(str(i)[0]) + int(str(i)[1]) < 9:
        print (i,end=" ")
    elif 100 <=i <= 999 and int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) < 9:
        print (i,end=" ")
        

