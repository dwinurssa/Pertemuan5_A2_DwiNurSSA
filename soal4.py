x = int(input("Masukkan total data : "))
total = 0

for i in range(0, x):
    jum = int(input("Masukkan nilai ke-%d : " % (i+1)))
    total += jum
    rata = total/x
print("Nilai rata-ratanya adalah ", rata)