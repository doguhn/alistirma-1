x = input(str("Lütfen bir sayı giriniz= "))
if len(x)==3 :
          if x[0]==x[2]:
              print(x," palindromik bir sayıdır.")
          else:
              print(x," palindromik bir sayı değiltir.")

elif len(x)==4:
          if x[0]==x[3] and x[1]== x[2]:
              print(x," palindromik bir sayıdır.")
          else:
              print(x," palindromik bir sayı değildir.")
else:
          print("Lütfen 3 ya da 4 haneli bir sayı giriniz.")

          
