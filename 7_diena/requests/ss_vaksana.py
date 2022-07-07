import requests
import time
from bs4 import BeautifulSoup as bs

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

    for tabula in tabulas:
        print(tabula)
        print("==================================")
        print("==================================")
        print("==================================")
        print("==================================")
        print("==================================")
        print("==================================")




info("7_diena/requests/lapas/lapa_1.html")