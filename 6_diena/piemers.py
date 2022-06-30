summa = 0
skaits = 0

with open("titanic_1.csv", "r", encoding="utf-8") as f:
    rindinas = f.readlines()
    for rindina in rindinas:
        #print(rindina)
        kolonas = rindina.split(",")
        #print(kolonas)
        klase = kolonas[1]
        cena = float(kolonas[7])
        #print(cena)
        if klase == "3":
            summa = summa + cena
            skaits = skaits + 1
        #exit()

print(summa)
print(skaits)

print("Vidējā biļetes cena ir:", summa / skaits)