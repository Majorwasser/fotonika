from nauka import finał

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



def bierz_wartosci(finał):
    lewa = None
    Operator = None
    for cotojest in finał:
        if lewa != None and Operator != None and cotojest[0] == "NUMBER":
            return BinaryOp(left=lewa , op= Operator , right=Number(cotojest[1]))
        if cotojest[0] == "NUMBER" and Operator == None:
            lewa = Number(cotojest[1])
        if cotojest[0] == "PLUS":
            Operator = cotojest[1]
    
            

        



print (bierz_wartosci(finał))
    