with open ("plik.asm" , "r") as plik:
    linijki = plik.readlines()
    print(linijki)

stos =[]
def czytanielinijek (linijki):
    for yalla in linijki:
        if yalla.startswith("LOAD"):
            stos.append(float(yalla[4:]))
        if yalla.startswith("MUL"):
            b = stos.pop()
            a = stos.pop()
            stos.append(float(a) * float(b))
        if yalla.startswith("ADD"):
            b = stos.pop()
            a = stos.pop()
            stos.append(float(a) + float(b))
        return stos
            
print (czytanielinijek(linijki))