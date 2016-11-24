
def second():
    with open("input.txt", "r") as f:
        line = f.readlines()
    num = line[0].rstrip()
    maximum = max(num)
    with open("output.txt", "w+") as o:
        if len(num) == 1 or len(set(num.split(" "))) == 1:
            o.writelines("There is no second largest number.")
        else:
            o.writelines(max(x for x in num if x != maximum))

second()


