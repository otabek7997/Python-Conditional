import os
file = input("Fayl nomini kiriting: ")

if os.path.exists(file):
    print(f"Fayl '{file}' mavjud")
else:
    print(f"Fayl '{file}' topilmadi")     