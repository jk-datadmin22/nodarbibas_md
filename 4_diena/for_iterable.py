iepirkumi = ["sviests", "krejums", "piens", "biezpiens", "olas"]

print("Saraksta garums ir", len(iepirkumi))

for i in range(len(iepirkumi)):
    print(iepirkumi[i])
print("============================================")

for produkts in iepirkumi:
    print(produkts)

vards = "brīnumzeme"
for burts in vards:
    # if burts == "e":
    #     print("atradu e")
    print(burts, end = "-")
print()
print("============================================")