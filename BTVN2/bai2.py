day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

if month not in days_in_month or day < 1 or day > days_in_month[month]:
    print("Ngày hoặc tháng không hợp lệ")

elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print("Bạch Dương")

elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print("Kim Ngưu")

elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    print("Song Tử")

elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    print("Cự Giải")

elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    print("Sư Tử")

elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    print("Xử Nữ")

elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    print("Thiên Bình")

elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    print("Bọ Cạp")

elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    print("Nhân Mã")

elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    print("Ma Kết")

elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    print("Bảo Bình")

else:
    print("Song Ngư")