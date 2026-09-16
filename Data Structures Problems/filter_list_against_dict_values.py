roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

for k, v in sample_dict.items():
    if v in roll_number:
        roll_number.remove(v)
    else:
        pass
print(roll_number)