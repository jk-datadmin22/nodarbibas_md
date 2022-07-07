import requests
import json

URL = "https://api.chucknorris.io/jokes/random"

lapa = requests.get(URL)

if lapa.status_code == 200:
    print("Lapa veiksmīgi nolasīta!")
    saturs = lapa.text
    saturs = json.loads(saturs)
    print(saturs['id'])
    print(saturs['created_at'])
    print(saturs['value'])

else:
    print("Radās kļūda lapas pieprasīšanā. Kļūda:", lapa.status_code)

