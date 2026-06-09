from dataclasses import dataclass
from enum import Enum


class mozliwetypytokena (Enum):
    LPAREN = 1
    RPAREN = 2
    PLUS = 3
    STAR = 4
    NUMBER = 5


@dataclass
class Token:
    tokentype:mozliwetypytokena
    value: any
    

jan = Token(mozliwetypytokena.LPAREN , value = '(' )

print (jan.tokentype.name)
print (jan.tokentype.value)

   