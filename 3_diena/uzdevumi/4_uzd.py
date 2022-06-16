# Izveido gāzes kalkulatoru. Lietotājs ievada pateriņu (kWh) programma izvada 
# cik ir jāmaksā. 
# [Latvijas gāzes cenu tabula](https://lg.lv/majoklim/tarifi-un-kalkulators)

# Dabasgāzes gada patēriņš
#   0 - 2635 kWh (0 - 250 m³)
# 	2635.1 - 5269 kWh (250.01 - 500 m³)
# 	5269.1 - 263450 kWh (500.01 - 25000 m³)

# Tarifs par 1 kWh	0.1045819	0.0917141	0.0762993

paterins = int(input("Cik daudz gāzes tu patērēji šomēness?"))

gadaPaterins = paterins * 12

if gadaPaterins <= 2635:
    print("1. kategorijas tarifs")
    izmaksas = paterins * 0.1045819

elif gadaPaterins <= 5269:
    print("2. kategorijas tarifs")
    izmaksas = paterins * 0.0917141

else:
    print("3. kategorijas tarifs")
    izmaksas = paterins * 0.0762993

print("Tev šomēness jāmaksā ir", izmaksas)


if gadaPaterins <= 2635:
    print("1. kategorija")

if gadaPaterins > 2635 and gadaPaterins <= 5269:
    print("2. kategorija")

if gadaPaterins > 5269 and gadaPaterins <= 263450:
    print("3. kategorija")