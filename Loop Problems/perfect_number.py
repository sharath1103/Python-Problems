num = 28
divisor_num = 0
for i in range(1,(num//2)+1):
    if num%i == 0:
        divisor_num+=i
if divisor_num== num:
    print(f"{num} is a Perfect Number")
else:
    print(f"{num} is not a Perfect Number")