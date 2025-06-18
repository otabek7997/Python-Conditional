password = input("Parol yarating: ")

is_alpha = False
is_digit = False

if "A" <= password <= "Z" or "a" <= password <= "z" :
    is_alpha = True
    
if "1" <= password <= "9":
    is_digit = True

if len(password) >= 8 and is_alpha or is_digit:
    print("Parol qabul qilindi.")

else:
    print("Parol noto'g'ri. Kamida 8 belgi, 1 harf va 1 raqam bo'lishi kerak.")    
