print("1.balok")
p = int(input("masukan nilai panjang: "))
l = int(input("masukan nilai lebar: "))
t = int(input("masukan nilai tinggi: "))
volume_b = p * t
print("volume balok adalah",volume_b)

print("2.limas")
la =int(input("masukan nilai luas alas: "))
t =int(input("masukan nilai tinggi: "))
volume_la = 1/3 * la * t
print("volume limas adalah",volume_la)

print("3.tabung")
la = int(input("masukan nilai luas alas: "))
t = int(input("masukan nilai tinggi: "))
volume_t = la * t
print("volume tabung adalah",volume_t)

kursdolar = 14000
rupiah = float(input("masukan uang rupiah= "))
rupToDol = rupiah/kursdolar