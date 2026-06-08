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
@dataclass
class Variable:
    name:str
    
left = Number(3)
op = "*"
right = Number(4)










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
    
            

        



#print (bierz_wartosci(final))
    


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


print(parse_expression(final , 0 ))




node,_ = parse_expression(final , 0)
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

        
     

print (evaluate(node))