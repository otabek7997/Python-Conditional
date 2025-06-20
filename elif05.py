vazn = float(input("Vazn: "))
buy = float(input("Buy: "))

bmi = vazn / pow(buy, 2)

print(bmi)

if bmi < 18.5:
    print("Kam")
elif 18.5 <= bmi < 25:
    print("norm")
elif 25 <= bmi < 30:
    print("ortiqcha")
elif bmi >= 30:
    print("kaban")            