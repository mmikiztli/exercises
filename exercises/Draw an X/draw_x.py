
width = input("Enter the size of the X: ")
char = [" ", "*"]


def printed(space, midspace):
    print (char[0] * space + char[1] + char[0]
           * midspace + char[1] + char[0] * space)


def draw_x(width):
    while True:
        if width.isdigit() == False:
            width = input("Enter the size of the X: ")
        else:
            break
    space = 0
    midspace = int(width) - 2
    while midspace > 0:
        printed(space, midspace)
        space += 1
        midspace -= 2
    if midspace == 0:
        printed(space, midspace)
    elif int(width) % 2 != 0:
        print (char[0] * space + char[1])
        space -= 1
        midspace += 2
    while midspace <= int(width) - 2:
        printed(space, midspace)
        space -= 1
        midspace += 2

draw_x(width)
