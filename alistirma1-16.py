x = int(input("bir Sayı Giriniz ="))


n=0

for i in range (2,x):
    if x%i==0:
        n=1



if n==1:
    print(x,"bir asal sayı değildir.")
else:
    print(x,"bir asal sayıdır.")
