
def read_file(filename):
    with open(filename) as f:
        line = f.readlines()
    n = line[0].strip("\n").split(" ")
    a = line[1].strip("\n").split(" ")
    return a, n


def histogram(a, n):
    maximum = max(float(x) for x in a)
    minimum = min(float(x) for x in a)
    interval = float(maximum - minimum)
    scale = interval / float(n[0])
    bins = []
    intervals_dict = {}
    x = minimum
    while x <= maximum:
        bins.append(x)
        x += scale
    for i in range(1, len(bins)):
        intervals_dict.setdefault(bins[i], 0)
    for x in a:
        for i in range(1, int(n[0]) + 1):
            if float(x) < bins[i] and float(x) >= bins[i - 1]:
                intervals_dict[bins[i]] += 1
        if float(x) == maximum:
            intervals_dict[bins[-1]] += 1
    result = sorted(intervals_dict.items())
    with open("output.txt", "w+") as o:
        o.writelines(" ".join([str(x[1]) for x in result]))


def main():
    lines = read_file("histogram_input.txt")
    histogram(lines[0], lines[1])

if __name__ == "__main__":
    main()
