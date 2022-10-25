sayi = input("hesaplamak istediğiniz sayıyı giriniz")
sonuc = sayi #5
for x in range(1,int(sayi)+1):
  if int(sayi) > 1:
    sonuc = int(sonuc) * (int(sayi) - 1)
    sayi = int(sayi) - 1
  else:
    print(sonuc)
if int(sayi) ==  0:
  print("1")
if int(sayi) < 0:
  print("negatif bir sayi girdiniz.")