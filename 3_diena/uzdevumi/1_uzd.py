# Uzrakstiet programmu, kas prasa lietotājam ievadīt savu vārdu, 
# ja tas ievada vārdu, Bond, tad izdrukājiet uz ekrāna "Esi sveicināts 007", 
# ja cits tad "Esi sveicināts, VARDS", kur VARDS ir lietotāja ievadītais vārds.

vards = input("Ievadi savu vārdu:")

if vards == "Bond":
    print("Esi sveicināts, 007")
else:
    print("Esi sveicināts,", vards)

