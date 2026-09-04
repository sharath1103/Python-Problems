amount = int(input("Enter your income: "))
tax_payable = 0
if amount <= 10000:
    tax_payable = 0
elif amount <= 20000:
    tax_payable = (amount - 10000) * 0.1
else:
    tax_payable = (10000 * 0.1) + (amount - 20000) * 0.2
print("The tax payable is:", tax_payable)