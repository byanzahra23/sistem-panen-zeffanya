def hitung_total_panen(list_panen):
    return sum(list_panen)

print('Total Panen:', hitung_total_panen([100, 150, 200]), 'kg')

def hitung_diskon(total_harga, diskon_persen):
    return total_harga * (1 - diskon_persen / 100)

print('Harga setelah diskon: Rp', hitung_diskon(1000000, 10))
