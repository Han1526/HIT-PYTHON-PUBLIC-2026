month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))
if month < 1 or month > 12:
    print("Tháng không hợp lệ")

elif month in [1, 3, 5, 7, 8, 10, 12]:
    print("Số ngày:", 31)

elif month in [4, 6, 9, 11]:
    print("Số ngày:", 30)

else:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Số ngày:", 29)
    else:
        print("Số ngày:", 28)