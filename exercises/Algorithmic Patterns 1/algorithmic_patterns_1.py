

# iterate("b", {"a": "ab", "b": "a"}, 5)


def pattern(axiom, rules, num):
    result = axiom
    for i in range(int(num)):
        result = "".join(rules[ch] if ch in rules else ch for ch in result)
    return result

print (pattern("b", {"a": "ab", "b": "a"}, 5))
# abaababa
