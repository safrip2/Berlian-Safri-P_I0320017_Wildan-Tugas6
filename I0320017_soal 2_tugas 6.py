print("\t\tSelamat Datang")
print("masukkan angka untuk ditambahkan.")
print("masukkan 0 untuk berhenti")
a = 1
s = 0
count = 0
while a != 0:
    print("total sementara adalah", s)
    a = float(input("masukkan angka: "))
    s += a
    count += 1
print("jumlah total adalah ", s)
print(f"rata-rata adalah {round(s / (count -1), 2)}")