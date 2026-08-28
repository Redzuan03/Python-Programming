'''tup1 = (1,3,5,7) #menaip nombor
print(tup1) 

print(tup1[1]) #memanggil nilai untuk dimainkan di output dengan menggunakan index
print(tup1[3])
print(tup1[-1])
print(tup1[-2])'''

tup1 = (1,3,5,7,8,9,12,13) #menaip nombor
 
print(tup1[1:3]) 
print(tup1[0:2])
print(tup1[:3]) #starts dengan 0
print(tup1[1:8])
print(tup1[::3]) # nak jarak 2 nombor
print(tup1[2::2])#Mula drpd 5 dan selang satu per satu 
print(tup1[:-1])#semua item kecuali 13
print(tup1[3:-2])
print(tup1[-4:-2])
print(tup1[-4:6])
print(tup1[::-1])
print(tup1[::-4])

#Tuple boleh gabungan beberapa jenis
tup3 = ('Apple','Pear',1,'Lalalala')
for x in tup3:
    print(x)
