"""
if <boolean loģika>:
    komandas
    kas
    jāveic, ja loģika ir True
else:
    komands
    kas
    jāveic, ja loģika ir False

if <boolean loģika>:
    komandas
    kas
    jāveic, ja loģika ir True

if <boolean loģika>:
    komandas
    kas
    jāveic, ja loģika ir True
elif <boolean loģika>:
    komandas
    kas
    jāveic, ja loģika ir True
elif .......
    ....
    ....
....
    ....
    ....
else: # nav obligāts
    komandas
    kas
    jāveic, ja viss iepriekš bijis False

"""

vecums = int(input("Cik tev gadu?"))

if vecums >= 18:
    print("Apsveicu tu esi pilngadīgs!")
else:
    print("Tev vēl jāpaaugas!")

if vecums >= 65:
    print("Tev laiks doties pensijā!")


# if vecums < 10:
#     print("Pirmā desmitgade!")
# else:
#     if vecums < 20:
#         print("Otrā desmitgade")
#     else:
#         if vecums < 30:
#             print("Trešā desmitgade")
#         else:
#             .......

if vecums < 10:
    print("Pirmā desmitgade")
elif vecums < 20:
    print("Otrā desmitgade")
elif vecums < 30:
    print("Trešā desmitgade")
elif vecums < 40:
    print("Ceturtā desmitgade")
else:
    print("Nevaru noteikt desmitgadi")


# Saīsinātais pieraksts
print("Pilngadīgs") if vecums >= 18 else print("Paaudzies!")