money = int(input("Nhập số xu: "))
price = 28
beer = money // price
total = beer
empty = beer

while empty >= 3:
    new_beer = empty // 3
    total += new_beer
    empty = empty % 3 + new_beer

print("Tổng số chai bia có thể uống:", total)