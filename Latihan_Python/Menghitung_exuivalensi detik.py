jam=3600
menit=60
hari=86400

detik=int(input('Masukkan Detik :'))
jam = detik // 3600
sisa = detik % 3600

menit = sisa // 60
detik = sisa %60

hari = sisa // 86400
detik = sisa % 86400

print('jam	= ',jam)
print('menit 	=',menit)
print('detik 	=',detik)
print('hari 	=',hari)