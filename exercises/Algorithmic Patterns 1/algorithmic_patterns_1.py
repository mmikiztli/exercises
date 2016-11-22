

# iterate("b", {"a": "ab", "b": "a"}, 5)


def pattern(axiom, rules, num):
    result = [axiom]
    x = 0
    while x < int(num):
        for ch in axiom:
            for key, value in rules.items():
                if ch == key:
                    result.append(value)
        axiom = result[-1]
        x += 1
    return "".join(result[-num:])

print (pattern("b", {"a": "ab", "b": "a"}, 5))
# abaababa


