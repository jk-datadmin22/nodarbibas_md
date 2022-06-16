# Lietotājs ievada savu vērtējumu programmēšanā izvadīt 
# vārdisko vērtējumu (izcili, teicami utt.)


vertejums = int(input("Ievadi savu vērtējumu:"))

if vertejums == 10:
    print("Izcili")
elif vertejums == 9:
    print("Teicami")
elif vertejums == 8:
    print("Ļoti labi")
elif vertejums == 7:
    print("Labi")
elif vertejums == 6:
    print("gandrīz labi")
elif vertejums == 5:
    print("viduvēji")
elif vertejums == 4:
    print("gandrīz viduvēji")
elif vertejums == 3:
    print("vāji")
elif vertejums == 2:
    print("ļoti vāji")
elif vertejums == 1:
    print("ļoti, ļoti vāji")
else:
    print("Nespēju noteikt tavu vērtējumu.")