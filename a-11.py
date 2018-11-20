height = input('Height?')
weight = input('weight')

bmi = round(int(weight) / (float(height) ** 2), 2)
print('your bmi is ', bmi)
