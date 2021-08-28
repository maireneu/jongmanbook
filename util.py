
def readInput(filename):
    r = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            r.append(line.strip().replace('\t', ' ').split(' '))
    return r
