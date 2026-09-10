binary_str = "1101"
decimal_val = 0
reversed_binary = binary_str[::-1]
for i in range(len(reversed_binary)):
    if reversed_binary[i] == '1':
        decimal_val+=2**i
print(decimal_val)