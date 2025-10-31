modal_awal = 100000000
total_laba = 0

for bulan in range(1, 9):
    if bulan == 1 or bulan == 2:
        laba = 0
    elif bulan == 3:
        laba = modal_awal * 0.01
    elif bulan >= 4 and bulan <= 5:
        laba = modal_awal * 0.05
    elif bulan >= 6 and bulan <= 7:
        laba = modal_awal * 0.05
    elif bulan == 8:
        laba = modal_awal * 0.03

    print(f"laba bulan ke- {bulan} sebesar: {int(laba)}")
    total_laba += laba

print(f"\nTotal laba adalah: {int(total_laba)}")
