def f(x):
    return x + 5

def superMatematika(skaitlis):
    rezultats = skaitlis + 5
    return rezultats

#print(f(5))
#print(superMatematika(5))
#print(f(7))

# def funkcijasNosaukumu(arguments1, arguments2, ....):
#     darbības, kuras
#     vēlamies veikt

#     return atgriezamaVertiba

def sasveicinaties():
    print("Esi sveiks! 1")

def sasveicinaties2():
    return "Esi sveiks! 2"

def sasveicinaties3():
    return ""    

sasveicinaties()
print(sasveicinaties2())
print(sasveicinaties())

print("=================================")

def saskaitit(skaitlis1, skaitlis2):
    sum = skaitlis1 + skaitlis2
    return sum

a = 4
b = 3
print(saskaitit(2, 3))
print(saskaitit(7, 3))

rezultats = saskaitit(a, b)
print(rezultats)
b = 9

rezultats = saskaitit(15, b)
print(rezultats)