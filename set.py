mySet = {"Engin","Derin","Salih","Ahmet"}
print(mySet)

for my in mySet:
  print(my)

print("Derin" in mySet)

if "Derin" in mySet:
  print("listede var")
else:
  print("listede yok")

mySet.add("Ali")
print(mySet)

mySet.remove("Ali")
print(len(mySet))

del mySet

#set union 2 setin elemanlarının kesişimlerini sadece 1 kere alarak setlerin elemanlarını  birleştirir
setA = {1,2,3,4,5,6,7,9}
setB = {1,3,4,5,7,8}

setC = (setA.union(setB)).copy()
print(setA | setB)
print(setC)



#set intersection: setlerin sadece kesişimlerini alır
print(setA & setB)
print(setA.intersection(setB))

#set Difference: belirtilen sette olup diğer sette olmayan elemanları gösterir
print(setA - setB)
print(setA.difference(setB))

#set symmetic difference : 2 setin kesişimi haricindeki bütün elemanları alır
print(setA ^ setB)
print(setA.symmetric_difference(setB))