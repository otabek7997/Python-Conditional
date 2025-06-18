temperature = float(input("Havo haroratini kiriting: "))

if temperature < 0:
    print("Juda sovuq! Issiq kiyim kiying")

if 0 < temperature < 14:
    print("Sovuq. Kurtka kiying")

if temperature >= 15:
    print("Ob-havo yaxshi")    