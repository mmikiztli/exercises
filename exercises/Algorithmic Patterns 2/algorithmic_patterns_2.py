from tkinter import *
from turtle import *


def pattern(axiom, rules, num):
    result = [axiom]
    x = 0
    while x < int(num):
        for ch in axiom:
            for key, value in rules.items():
                if ch == key:
                    result.append(value)
        x += 1
    return "".join(result)

res = pattern("F++F++F", {"F": "F−F++F−F", "-": "-", "+": "+"}, 10)

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
