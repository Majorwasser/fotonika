text = "2+3"

def sprawdz_cotojest(text):
    if text.isalpha():
        print (f"Znak '{text}' to litera")
    elif text.isdigit():
        print(f"Znak '{text}' to liczba")


    for znak in text:
        print(znak)

    

sprawdz_cotojest(text)
    