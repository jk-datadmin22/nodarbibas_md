from operator import index


iepirkumi = ["sviests", "krejums", "piens", "biezpiens", "olas"]
#               0           1           2         3         4
#print(type(iepirkumi))
print(iepirkumi)
print(iepirkumi[2])

iepirkumi.append("eļļa")
print(iepirkumi)

iepirkumi.remove("piens")
print(iepirkumi)


iepirkumi.pop()
iepirkumi.pop(0)
print(iepirkumi)

indeks = iepirkumi.index("olas")
print(indeks)

if "biezpiens" in iepirkumi:
    print("Jā biezpiens ir iepirkumos!")

if "pica" in iepirkumi:
    print("Jā pica ir iepirkumos!")
else:
    iepirkumi.append("pica")

print("Saraksta garums ir",len(iepirkumi))

print(iepirkumi)

iepirkumi.sort()

print(iepirkumi)



