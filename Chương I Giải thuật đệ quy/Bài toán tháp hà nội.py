def thap_ha_noi(n, nguon, dich, trung_gian):
    if n == 1:
        print('Chuyển đĩa 1 từ cọc', nguon, 'sang cọc', dich)
    else:
        thap_ha_noi(n-1, nguon, trung_gian, dich)
        print('Chuyển đĩa', n, 'từ cọc', nguon, 'sang cọc', dich)
        thap_ha_noi(n-1, trung_gian, dich, nguon)

n = int(input('n = '))
thap_ha_noi(n, 'A', 'B', 'C') 

