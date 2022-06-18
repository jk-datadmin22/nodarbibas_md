summa = 0
skaits = 0
while True:
    skaitlis = int(input("Ievadi skaitli:"))
    if skaitlis == 0:
        break
    
    if skaitlis % 2 == 0:
        summa = summa + skaitlis
        skaits = skaits + 1

if skaits != 0:
    print("Vidējais ir", summa / skaits)
else:
    print("Netika ievadīts neviens pāra skaitlis!")