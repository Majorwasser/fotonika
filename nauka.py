text = "2+3"

lexer = ["LPAREN" , "NUMBER" , "PLUS" , "RPAREN" , "STAR" , "IDENTIFIER","MINUS"]

def sprawdz_cotojest(text):
    if text.isalpha():
        return(lexer[5] , text)
    elif text.isdigit():
        return(lexer[1] ,text)
    elif text == "+":
        return(lexer[2], text)
    elif text =="*":
        return(lexer[4],text)
    elif text == " "  :
        pass
    elif text == "(":
        return(lexer[0], text)
    elif text == ")":
        return(lexer[3],text)
    elif text == "-":
        return(lexer[6],text)
    

    

finał =[]
for pojedynczo in text:      
    wynik = sprawdz_cotojest(pojedynczo)
    if wynik != None:
        finał.append(wynik)
        
print(*finał)     
       


    