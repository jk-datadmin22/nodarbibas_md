import requests

ADRESE = "https://www.ss.lv/lv/transport/cars/today/"

def saglabat_lapu(adrese, fails):
    pieprasijums = requests.get(adrese)

    if pieprasijums.status_code == 200:
        lapa = pieprasijums.text

        with open(fails, "w", encoding="utf-8") as f:
            f.write(lapa)

    else:
        print("Radās kļūda lapas pieprasīšanā! Kods:", pieprasijums.status_code)
        return


saglabat_lapu(ADRESE, "7_diena/requests/lapas/lapa_1.html")
