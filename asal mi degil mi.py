def asal(sayi):
  #sayi = int(input("sayiyi giriniz"))
  sayac = sayi - 1
  sonuc = bool()

  for x in range(sayi):
    if sayi % sayac !=0:
      sayac = int(sayac - 1)
      if sayac == 1:
        sonuc = True
        break
    else:
      sonuc= False
      break
    
  return sonuc
sonuc= asal(61)
print(sonuc)