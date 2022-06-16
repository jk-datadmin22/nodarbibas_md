# Izveido programmu, kas nosaka vai lietotāja ievadītais skaitlis ir pāra vai nepāra.

skaitlis = int(input("Ievadi skaitli:"))

if skaitlis % 2 == 0:
    print("Ievadītais skaitlis ir pāra skaitlis.")
else:
    print("Ievadītais skaitlis ir NEpāra skaitlis.")