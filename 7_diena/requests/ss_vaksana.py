import requests
import time
from bs4 import BeautifulSoup as bs
import csv

def saglabat_lapu(adrese, fails):
    pieprasijums = requests.get(adrese)

    if pieprasijums.status_code == 200:
        lapa = pieprasijums.text

        with open(fails, "w", encoding="utf-8") as fails:
            fails.write(lapa)

    else:
        print("Radās kļūda lapas pieprasīšanā! Kods:", pieprasijums.status_code)

ADRESE = "https://www.ss.lv/lv/transport/cars/today/"

def atvilkt_lapas(daudzums):
    for i in range(1, daudzums + 1):
        adrese = f"{ADRESE}page{i}.html"
        fails = f"7_diena/requests/lapas/lapa_{i}.html"

        print("Pieprasījums uz", adrese, "--->", fails)
        saglabat_lapu(adrese, fails)

        time.sleep(2)

# atvilkt_lapas(46)

def info(htmlDatne):
    with open(htmlDatne, "r", encoding="utf-8") as f:
        html = f.read()

    zupa = bs(html, "html.parser")

    tabulas = zupa.find_all("table")
    
    autoTabula = tabulas[4]

    autoRindas = autoTabula.find_all("tr")

    dati = []

    for rinda in autoRindas[1:-1]:
        auto = {}
        # print(rinda)
        # print("========================")
        # print("========================")
        # print("========================")

        lauki = rinda.find_all("td")

        if lauki[4].text == "-" or lauki[6].text == "-" or not lauki[3].br:
            continue
        
        auto['gads'] = lauki[4].text

        tilpums = lauki[5].text

        if "D" in tilpums:
            auto["dzinejs"] = "dīzelis"
            auto["tilpums"] = tilpums[:-1]
        elif "H" in tilpums:
            auto["dzinejs"] = "hibrīds"
            auto["tilpums"] = tilpums[:-1]
        elif "E" in tilpums:
            # ignorejam elektromobilus
            continue
        else:
            auto["dzinejs"] = "benzīns"
            auto["tilpums"] = tilpums

        auto["nobraukums"] = lauki[6].text.replace(" tūkst.", "")

        auto["cena"] = lauki[7].text.replace(",","").replace("  €","").replace("maiņai", "")

        lauki[3].br.replace_with("!")
        auto["marka"] = lauki[3].text.replace("!", " ")
        auto["razotajs"] = lauki[3].text.split("!")[0]
        auto["modelis"] = lauki[3].text.split("!")[1]

        #print(auto)
        #exit()

        dati.append(auto)

    return dati

def saglabat_datus(autoDati):
    with open("7_diena/requests/ss_auto.csv", "w", encoding="utf-8", newline="") as f:
        kolonas = ['razotajs', 'modelis', 'marka', 'gads', 'dzinejs', 'tilpums', 'nobraukums', 'cena']
        w = csv.DictWriter(f, fieldnames=kolonas)
        w.writeheader()

        for auto in autoDati:
            w.writerow(auto)


def izvilkt_datus(daudzums):
    visiDati = []
    for i in range(1, daudzums + 1):
        fails = f"7_diena/requests/lapas/lapa_{i}.html"
        datnesDati = info(fails)
        visiDati = visiDati + datnesDati

    saglabat_datus(visiDati)


izvilkt_datus(46)