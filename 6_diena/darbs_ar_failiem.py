saraksts = ["Māris", "Anna", "Krista"]

# režīmi: r - lasīšana, w - rakstīšana (izdzēš visu saturu), a - pievienošana
with open("dati.txt", "a", encoding="utf-8") as fails:
    fails.write("Esi sveiks Māri!\n") # Kreisais Alt + ciparnīcā 92
    fails.write("Šodien apmācies laiks.\n")
    #fails.writelines(saraksts)
    fails.write("\n".join(saraksts))
    fails.write("\n")

# Nolasīt visu failu vienā simbolu virknē.
# with open("dati.txt", "r", encoding="utf-8") as fails:
#     saturs = fails.read()

# print(saturs)


# Lasīt pa rindiņai
# with open("dati.txt", "r", encoding="utf-8") as fails:
#     teksts1 = fails.readline()
#     teksts2 = fails.readline()


# print(teksts1)
# print(teksts2)

# Lasīt pa rindiņai
with open("dati.txt", "r", encoding="utf-8") as fails:
    rindina = fails.readline()
    while rindina:
        #print(rindina)
        rindina = fails.readline()

# Lasīt pa rindiņai
with open("dati.txt", "r", encoding="utf-8") as fails:
    rindinas = fails.readlines()
    #print(rindinas)

    for rindina in rindinas:
        print(rindina)