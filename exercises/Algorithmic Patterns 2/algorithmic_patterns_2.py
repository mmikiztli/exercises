from tkinter import *
from turtle import *


def pattern(axiom, rules, num):
    result = axiom
    for i in range(int(num)):
        result = "".join(rules[ch] if ch in rules else ch for ch in result)
    return result

res = pattern("F++F++F", {"F": "F−F++F−F"}, 1)

print (res)

setup()
clear()
for i in res:
    if i == "F":
        forward(25)
    elif i == "-":
        left(60)
    elif i == "+":
        right(60)
done()
