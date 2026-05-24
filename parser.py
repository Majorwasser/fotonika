matma = "2 + 3 * 4"

parser = ["3","*","4"]
plus = ["2","+"]
plus.append(parser)

print(plus)

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

print(t)