

lights = ["red","yellow","green"]

print("lutfen kırmızı için:0 \nsarı için:1\nyeşil için:2\nyi tuşlayınız:")
girdi = input()
sayac = 5
while True:
  if int(girdi) >= 3:
    print("yanlış bir değer girdiniz lütfen girdiğiniz değeri kontrol edip tekrar deneyiniz.")
    if sayac > 0:
      print("Kalan deneme hakkı:"+str(sayac))
      sayac = sayac - 1
      girdi = input()
    else:
      print("Deneme hakkınız kalmadı lutfen  15 dakika sonra tekrar deneyiniz!!!")
      break
  else:
    break
  

if int(girdi) < 3:
  currentlight = lights[int(girdi)]
  print(currentlight)
  
  if currentlight == "red":
    print("stop!")

  elif currentlight == "yellow":
    print("ready!")

  elif currentlight == "green":
    print("go")
  