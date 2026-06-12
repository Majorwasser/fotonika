with open ("plik.asm" , "r") as plik:
    linijki = plik.readlines()
    print(linijki)

stos =[]
def czytanielinijek (linijki):
    for yalla in linijki:
        if yalla.startswith("LOAD"):
            stos.append(yalla[4:])
            
    