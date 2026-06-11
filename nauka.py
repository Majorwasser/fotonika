from dataclasses import dataclass
    
@dataclass
class Number:
    value:float
@dataclass
class BinaryOp:
    
    left:str
    op:str
    right:str
@dataclass
class Variable:
    name:str
    
left = Number(3)
op = "*"
right = Number(4)



def parse_factor(final ,i):
    if final[i][0] =="NUMBER":
        return(Number(float(final[i][1])) , i+1)
    if final[i][0] == "LPAREN":
        wezel , nowy_i = parse_expression(final , i+1)
        return(wezel , nowy_i +1)
    if final[i][0] == "IDENTIFIER":
        return(Variable(final[i][1]) , i+1)
    




def parse_term (final , i):
    
    
    wezel , nowy_i = parse_factor(final , i)
    if  i+1 < len(final) and final[nowy_i][0] =="STAR" :
        wezel_prawy , nowy_i =parse_factor(final, nowy_i+1)
        return (BinaryOp(left=wezel , op="*" , right=wezel_prawy), nowy_i)
    elif i+1 < len(final) and final[nowy_i][0] == "PLUS":
        return (wezel , nowy_i)
    return (wezel , nowy_i)





def parse_expression (final , i):
    
    wezel , nowy_i = parse_term(final , i)
    if nowy_i <len(final) and final[nowy_i][0] =="PLUS":
        wezel_prawy , nowy_i =parse_term(final , nowy_i +1)
        return (BinaryOp(left=wezel , op="PLUS" , right= wezel_prawy) , nowy_i)
    elif nowy_i <len(final) and final[nowy_i][0] =="STAR":
        return parse_term(final , nowy_i)
    return (wezel   , nowy_i)        


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






def evaluate(node):
        
        if isinstance(node , Number):
            return node.value
        elif isinstance(node , BinaryOp):
            
            lewastrona = node.left
            operator = node.op
            prawastrona = node.right        
            lewawartosc = evaluate (lewastrona) 
            prawawartosc = evaluate(prawastrona)
            if operator == "PLUS":
                return lewawartosc + prawawartosc
            elif operator == "*":
                return lewawartosc * prawawartosc
        elif isinstance(node , Variable):
                zmienna = node.name
                slownik = {"x":5}
                return slownik[zmienna]
        
def compile(node):
    listainstrukcji = ["LOAD" , "ADD" , "MUL"]

    if isinstance(node , Number):
        return ["LOAD" + str(node.value)]
    elif isinstance(node , BinaryOp):
        operator =node.op
        if operator=="PLUS":
            lewastrona = compile(node.left)
            prawastrona = compile(node.right)
            plusik = ["ADD"]

            outro = lewastrona + prawastrona + plusik
            return outro
        if operator == "*":
            lewastrona = compile(node.left)
            prawastrona = compile(node.right)
            gwiazdka = ["MUL"]

            finisz = lewastrona + prawastrona + gwiazdka
            return finisz
        








        
    

        



while True:

    text = input( "wpisz wyrazenie ale proste:" )


    final =[]
    for pojedynczo in text:      
        wynik = sprawdz_cotojest(pojedynczo)
        if wynik != None:
            final.append(wynik)
            
    print(*final)

    print(parse_expression(final , 0 ))
    node,_ = parse_expression(final , 0)
    print (evaluate(node))
    print (compile(node))
    instrukcje = compile(node)
    with open("plik.asm" , "w" czy) as plik:
        for elementy in instrukcje:
            plik.write(f"instrukcje to: {elementy}\n")







    


    

            
        

    