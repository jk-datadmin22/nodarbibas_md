"""
== - salīdzināšanas operators, vai ir vienāds
!= - salīdzināšanas operators, vai ir nevienāds
<  - mazāks par
>  - lielāks par
<= - mazāks vai vienāds
>= - lielāks vai vienāds

"""

sk1 = 13
sk2 = 7
sk3 = 7

print("sk1==sk2", sk1 == sk2)
print("sk1!=sk2", sk1 != sk2)

print("=============================================")
print("sk1 < sk2", sk1 < sk2)
print("sk1 > sk2", sk1 > sk2)
print("sk1 <= sk2", sk1 <= sk2)
print("sk1 >= sk2", sk1 >= sk2)

print("=============================================")
print("sk3 < sk2", sk3 < sk2)
print("sk3 > sk2", sk3 > sk2)
print("sk3 <= sk2", sk3 <= sk2)
print("sk3 >= sk2", sk3 >= sk2)

print("=============================================")

vards1 = "Maris"
vards2 = "maris"
vards3 = "maris"


print("Maris == maris", vards1 == vards2)
print("maris == maris", vards3 == vards2)

print("=============================================")
# mArIs
print("visi mazie pārbaude", vards1.casefold() == vards2.casefold())
print("visi mazie pārbaude", vards1.lower() == vards2.lower())

patiesiba = True
meli = False

print("patiesiba != meli", patiesiba != meli)


"""
AND - skatās vai abas puses ir True
OR - vai kāda no pusēm ir True

A       B       A and B     A or B      A == B
True    False   False       True        False
False   True    False       True        False
True    True    True        True        True
False   False   False       False       True

"""

sk1 = 1
sk2 = 2
sk3 = 3
sk4 = 3

# sk1 < sk2 < sk3 - tā nedarīt
# sk1 < sk2 and sk2 < sk3

print("Rezultats AND:", sk2 > sk1 and sk3 == sk4)
print("Rezultats AND:", sk2 < sk1 and sk3 == sk4)

print("Rezultats OR:", sk2 > sk1 or sk3 == sk4)
print("Rezultats OR:", sk2 < sk1 or sk3 == sk4)

