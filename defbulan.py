def input_bulan():
    while True:
        month = int(input("Masukkan bulan (1-12): "))
        if month in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            return month
        else:
            print("*Salah memasukkan nilai bulan: ", month, " *")
            
def menentukan_hari_dalam_bulan(month):
    if month == 0:
        return "Terima kasih sudah menggunakan program ini."
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return "Ada 31 hari dalam bulan ini"
    elif month in  [4, 6, 9, 11]:
        return "Ada 30 hari dalam bulan ini"
    elif month == 2:
        year = int(input("Masukkan tahun (e.g., 2023): "))
        if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
            return "Ada 29 hari dalam bulan ini"
        else:
            return "Ada 28 hari dalam bulan ini"
        
bsn = False
print("Program ini akan menentukan jumlah hari dalam bulan tertentu")
while not bsn:
    print("Masukkan 0 untuk menghentikan program")
    month = input_bulan()
    result = menentukan_hari_dalam_bulan(month)
    print(result)
    if month == 0:
        bsn = True
    