from nauka import final

matma = "2 + 3 * 4"

parser = ["3","*","4"]
plus = ["2","+"]
plus.append(parser)

#print(plus)

from dataclasses import dataclass
@dataclass
class Number:
    value:float
@dataclass
class BinaryOp:
    
    left:str
    op:str
    right:str
    
left = Number(3)
op = "*"
right = Number(4)


t = BinaryOp( 
left = left,
op = op,
right = right,
)

węzeł_mnożenia = BinaryOp(left=Number(3) , op ="*", right =Number(4))
węzeł_dodawania = BinaryOp(left=Number(2) , op ="+" , right=węzeł_mnożenia)


#print(węzeł_dodawania)

#for typ , wartosc in finał
#if typ =="NUMBER":
#liczba = int(wartosc)
#print(liczba)




def bierz_wartosci(final):
    lewa = None
    Operator = None
    for cotojest in final:
        if lewa != None and Operator != None and cotojest[0] == "NUMBER":
            return BinaryOp(left=lewa , op= Operator , right=Number(cotojest[1]))
        if cotojest[0] == "NUMBER" and Operator == None:
            lewa = Number(cotojest[1])
        if cotojest[0] == "PLUS":
            Operator = cotojest[1]
        if cotojest[0] == "STAR":
            Operator = cotojest[1]
    
            

        



print (bierz_wartosci(final))
    


def parse_factor(final , i):
    if final[i][0] =="NUMBER":
        return(Number(final[i][1]))
    if final[i][0] == "LPAREN":
        return parse_expression(final , i+1)
    




def parse_term (final , i):
    
    lewa = parse_factor(final , i)
    if  i+1 < len(final) and final[i +1][0] =="STAR" :
        prawa =parse_factor(final, i+2)
        return BinaryOp(left=lewa , op="*" , right=prawa)
    elif i+1 < len(final) and final[i+1][0] == "PLUS":
        return lewa
    return lewa

    



def parse_expression (final , i):
    
    habibi = parse_term(final , i)
    if final[i+1][0] =="PLUS":
        yalla =parse_term(final , i+2)
        return BinaryOp(left=habibi , op="PLUS" , right= yalla)
    elif final[i+1][0] =="STAR":
        return parse_term(final ,i)
    return habibi            


print(parse_expression(final , 0 ))