# break - iziet ārā no cikla
# continue - pārpiet pie nākamās iterācijas (cika izpildes reizes)

skaitli = [1, 5, 2, 6, 3, 9, 7, 4, 8]


for skaitlis in skaitli:
    print(skaitlis, end = " ")

print()
print("===================================")

for skaitlis in skaitli:
    if skaitlis == 9:
        break
    print(skaitlis, end = " ")

print()
print("===================================")

for skaitlis in skaitli:
    print(skaitlis, end = " ")
    if skaitlis == 9:
        break    

print()
print("===================================")

for skaitlis in skaitli:
    if skaitlis == 9:
        continue
    print(skaitlis, end = " ")

print()
print("===================================")

for skaitlis in skaitli:
    print(skaitlis, end = " ")
    if skaitlis == 9:
        continue    

print()
print("===================================")


for i in range(10):
    if i == 5:
        continue
    print(i, end = " ")