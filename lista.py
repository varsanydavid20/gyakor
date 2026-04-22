X=float(input("Add meg a termék árát: "))
Y=float(input("Add meg hogy mennyi százalék kedvezményt kap: "))

vegosszeg = X * (1 - Y / 100)

print("Végösszeg:", vegosszeg, "Ft")