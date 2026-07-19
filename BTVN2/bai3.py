n = int(input("Nhập số nguyên: "))
temp = abs(n)
count = len(str(temp))
total = 0
for digit in str(temp):
    total += int(digit)

if n < 2:
    prime = False
else:
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break

print("Số chữ số:", count)
print("Tổng chữ số:", total)

if prime:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")