balance = 5000
yechib_olmoqchi = float(input("Yechib olinadigan miqdor: "))

if 0 < yechib_olmoqchi <= balance:
    print(f"Pul yechildi. Qolgan balans: {balance - yechib_olmoqchi} so'm")
else:
    print("Mablag' yetarli emas. Sizning balansingiz: 5000 so'm")
if yechib_olmoqchi < 0:
    print("Manfiy miqdor kiritib bo'lmaydi")    