import math

# + saskaitīt
# - atņemt
# * reizināt
# / dalīt
# // dalīt bez atlikuma
# % modulis
# ** kāpināšana

print(5 + 3)
print(7 - 4)
print("=====================")

sk1 = 13
sk2 = 5

print("sk1 =", sk1, "sk2 =", sk2)
print("Summa ir", sk1 + sk2)
print("Starpība ir", sk1 - sk2)
print("Reizināšana ir", sk1 * sk2)
print("Dalīšana ir", sk1 / sk2)

print("Dalīšana bez atlikuma ir", sk1 // sk2)
print("Modulis ir", sk1 % sk2)
# 13 // 5 => 2
# 2 * 5 = 10
# 13 - 10 ==> 3 <==


print("Kāpināšana", sk1 ** 2)

rezulats = 9 / 7
print("Rezultats", rezulats)
print("Rezultats", round(rezulats, 4))

sk3 = 225
print("Kvadratsakne", math.sqrt(sk3))

print("Pi skaitlis", math.pi)
print("Pi skaitlis", round(math.pi, 2))