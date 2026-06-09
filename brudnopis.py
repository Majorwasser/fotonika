from enum import Enum

class mozliwosocitokenow(Enum):
    NUMBER = 1
    LPAREN = 2



from dataclasses import dataclass
@dataclass
class  Token:
    tokentype:mozliwosocitokenow
    wartosci:any

jan = Token(mozliwosocitokenow.LPAREN , wartosci=3)

print (jan.tokentype.name)
print (jan.tokentype.value)
print (jan.tokentype)