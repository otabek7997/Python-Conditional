num_1 = int(input("raqam 1:"))
num_2 = int(input("raqam 2:"))
amallar = (input("kiriting:"))


if amallar == '+':
    print(f'{num_1+num_2}')
elif amallar == '-':
    print(f'{num_1-num_2}')

elif amallar ==' /':
    if num_2 == 0:
        print('Xatolik nolga bulish mumkinmas')
    else:
        print(f'{num_1/num_2}')
else:
    print("xatolik")
    




