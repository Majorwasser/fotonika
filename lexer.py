from enum import Enum 
from dataclasses import dataclass
class TOKENTYPE(Enum):
    NUMBER = 1
    PLUS = 2
    STAR = 3
    MINUS = 4
    SLASH =5
    LPAREN = 6
    RPAREN = 7
    IDENTIFIER = 8

@dataclass
class Token:
    type : TOKENTYPE
    value: str

t = Token(type = TOKENTYPE.NUMBER , value = "x")
print (t)