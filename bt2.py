# Tao list
lst_data = [i for i in range(1, 13) if i%2 == 0]
print(lst_data)
# Xoa phan tu chia het cho 3
i = 0
end = len(lst_data)
while i <= end:
    if lst_data[i] % 3 == 0:
        lst_data.pop(i)
        end -= 1
    i += 1
print(lst_data)
# Them phan tu
lst_data.extend([1, 2, 3])
for i in range(8, 5, -1):
    lst_data.insert(3, i)
print(lst_data)
# Chuyen cac so chia het cho 2 va 5 thanh 0
for i in range(len(lst_data)):
    if lst_data[i] % 2 == 0:
        lst_data[i] = 0
    elif lst_data[i] % 5 == 0:
        lst_data[i] = 0
print(lst_data)
# OUTPUT
# [2, 4, 6, 8, 10, 12]
# [2, 4, 8, 10]
# [2, 4, 8, 6, 7, 8, 10, 1, 2, 3]
# [0, 0, 0, 0, 7, 0, 0, 1, 0, 3]