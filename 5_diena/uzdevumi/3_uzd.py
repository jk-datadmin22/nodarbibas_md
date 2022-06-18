# Izveido programmu, kur lietotājam ir jāuzmin datora iedomātais 
# skaitlis (no 1 līdz 20). Lietotājs min tik ilgi, 
# kamēr ir atminējis skaitli, beigās parāda tekstu "Apsveicam ar uzvaru!" 
# un rezultātu (minējuma skaitu).
import random

skaitlis = random.randint(1, 20) # datora iedomātais skaitlis
meginajumi = 0

while True:
    try:
        minejums = int(input("Ievadi skaitli, kuru gribi uzminēt (0 - iziet):"))
    except:
        print("Ievade ir nepareiza...")
        continue
    
    meginajumi = meginajumi + 1

    if minejums == 0:
        print("Man žēl, ka tu padevies!")
        break

    if minejums == skaitlis:
        print("Apsveicam ar uzvaru!")
        print("Lai uzvarētu tev tas prasīja", meginajumi, "mēģinājumus.")
        break
    else:
        if minejums > skaitlis:
            print("Tavs minējums ir par augstu!")
        else:
            print("Tavs minējums ir par zemu.")
        print("Mēģini vēlreiz ...")