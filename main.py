import random

# Szavak betöltése

szavak = []
f = open("magyar_szavak.txt", "r", encoding="utf-8")
for szo in f:
    szavak.append(szo.strip())

# Random szó kiválasztása
idx = random.randint(0, len(szavak) - 1)
gondoltSzo = szavak[idx]

# Játék
hibak = 0
MAX_HIBA = 6
tippek = []
kitalalt = False

while not (hibak > MAX_HIBA or kitalalt):
    # Kiirás
    print(f"Eddigi hibáid: {hibak}")
    print(" ".join(tippek))
    for betu in gondoltSzo:
        if betu in tippek:
            print(f"{betu} ", end="")
        else:
            print("_ ", end="")
    print()

    # Bekérés
    tipp = input("Adj meg egy tippet! ")
    if tipp != "":
        tipp = tipp[0].upper()
        if tipp not in gondoltSzo and tipp not in tippek:
            hibak = hibak + 1
        if tipp not in tippek:
            tippek.append(tipp)

    # Nyertes ellenőrzés
    db = 0
    for betu in gondoltSzo:
        if betu in tippek:
            db = db + 1
    kitalalt = db == len(gondoltSzo)

# Vége
print(f"Erre gondoltam: {gondoltSzo}")
if hibak <= MAX_HIBA:
    print("Nyertél!")
else:
    print("Leközelebb sikerül!")