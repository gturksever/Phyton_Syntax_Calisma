ogrenciler = ["Engin","Derin","Salih"]
ogrenciler.append("Ahmet")        #listenin sonuna eleman ekler
print(ogrenciler[3]) 
ogrenciler.remove(ogrenciler[0])  #listeden eleman siler 
ogrenciler.remove("Derin")        #listeden elemanın adıyla eleman siler
print(ogrenciler)
print(len(ogrenciler))

#list constructor(liste oluşturucu)
sehirler = list(("Ankara","İstanbul","Ankara"))
print(sehirler)
print(len(sehirler))

#diğer fonksiyonlar

#print(sehirler.clear()) listedeki bütün elemanları siler

print("Dizideki Ankara sayısı:"+str(sehirler.count("Ankara"))) # aratılan elemanın kaç tane olduğunu söyler

print("Ankara indexi: "+str(sehirler.index("Ankara"))) #aranılan ilk bulduğu elemanın dizide kaçıncı indexte tutulduğunu belirtir

sehirler.pop(1)               #girilen indexi siler

sehirler.insert(0,"İstanbul") # belirtilen indexe belirtilen elemanı ekler

sehirler.reverse()            #listeyi ters çevirir

sehirler2 = sehirler.copy()   # kopyasını al
sehirler2[0] ="İzmir"
print(sehirler2)
print(sehirler)

sehirler.extend(sehirler2)    # 2 diziyi birbiriyle birleştirir
print(sehirler)

sehirler.sort()               # dizinin elemanlarını alfabetik olarak sıralar
sehirler.reverse()            # bu şekilde ters alfabetik yapabiliriz
print(sehirler)