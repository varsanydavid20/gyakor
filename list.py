# 3 autó adatainak bekérése

autok = []

for i in range(1, 4):
    print(f"
{i}. autó adatai:")
    tipus = input("Típus: ")
    szin = input("Szín: ")
    ar = input("Ár: ")
    
    auto = {
        "típus": tipus,
        "szín": szin,
        "ár": ar
    }
    autok.append(auto)

# Az autók adatainak kiírása
print("
--- Bevitt autók adatai ---")
for i, auto in enumerate(autok, 1):
    print(f"{i}. autó: {auto['típus']} - {auto['szín']} - {auto['ár']} Ft")
