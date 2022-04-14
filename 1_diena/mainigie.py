# mainīgie
# mainīga nosaukums
# mainīgā vertība
# mainīga datu tips

vards = "Māris" # mainīgā nosaukums ir vards, mainīgā vērtība ir Māris
print(type(vards)) # mainīgā datu tips ir <class 'str'> jeb string (simbolu virkne)

# vienādības zīme = ir operators - piešķiršanas operatoru
uzvards = "Danne"
vertejums = 10
temperatura = 23.4
irBrilles = True

print("uzvards")
print(uzvards)
print(vertejums)
print(temperatura)
print(irBrilles)

print(type(uzvards)) # datu tips str - string, jeb simbolu virkne
print(type(vertejums)) # datu tips int - integer, jeb veseli skaitļi
print(type(temperatura)) # datu tips float - float, jeb racionāli skaitļi (ar komatiem)
print(type(irBrilles)) # datu tips bool - boolean, var saturēt True vai False

skaitlis = 5
otrsSkaitlis = "7"

print(skaitlis)
print(otrsSkaitlis)

# Mainīgo nosaukumi (vadlīnijas) https://www.python.org/dev/peps/pep-0008/
# - mainīgo nosaukumi jāveido tādi, lai tas parādītu, ko tie satur
# - jāizvairās no mainīgo nosaukumiem, kas satur tikai vienu burtu, piemēram, x, y, z....
# - mainīgo nosaukumā var būt cipars, bet mainīgā nosaukums NEVAR sākties ar ciparu
vards1 = "Māris"
vards2 = "Anna"
# 1vards = "Pēteris" šādi nevar

# - mainīgo nosaukumus jāsāk ar mazo burtu, ja tas satur vairākus vārdus izmantojam camelCase
camelCaseStyle = "stils"
snake_case_style = "stils"

# snakecasestyle = "stils" šādi nevajag

# - ja veidojam konstantes vai mainīgos, kas satur vienu vērtību, tad lietojam visus lielos burtus un atstarpē apakšsvītru
GRAVITACIJAS_PAATRINAJUMS = 9.8

# - mainīgo nosaukumu veidošanā NEIZMANTOJAM mīkstinājuma zīmes un garumzīmes un atstarpes.

# vārds = "123" šādi nedarīt !!!


mansVards = "Pēteris"
print(mansVards)

mansVards = "Juris"
print(mansVards)

print(vards, uzvards, vertejums, irBrilles)
print("Vārds:", vards, "Vērtējums:", vertejums)
print("Uzvārds:", uzvards)

print("Vārds:{vards}, Uzvārds:{uzvards}, Vērtejums:{vertejums}")
print(f"Vārds:{vards}, Uzvārds:{uzvards}, Vērtejums:{vertejums}")