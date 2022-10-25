matris1 =      [3,4,5],[6,7,8],[9,1,2]
matris2 =      [9,1,2],[5,7,3],[6,8,4]
matrisToplam = [[0]*3]*4

for i in range(3):
  for j in range(3):
    deger1 = int(matris1[i][j])
    deger2 = int(matris2[i][j])
    deger3 = deger1 + deger2
    matrisToplam[i][j] = int(deger3)


print(matrisToplam)
    