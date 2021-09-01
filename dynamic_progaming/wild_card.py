import util


def wild_card_rec(wi: int, wl: list, ii: int, il: str):
    if wi == len(wl) and ii >= len(il):
        return True
    if wi >= len(wl) and ii < len(il):
        return False
    if wl[wi] == "?":
        return wild_card_rec(wi+1, wl, ii+1, il)
    if wl[wi] == "*":
        for i in range(ii, len(il)+1):
            if wild_card_rec(wi+1, wl, i, il):
                return True
        return False
    if wi != len(wl) and ii >= len(il):
        return False
    if wl[wi] == il[ii:ii+len(wl[wi])]:
        return wild_card_rec(wi+1, wl, ii+len(wl[wi]), il)
    return False


def wild_card(pattern: str, match: str):
    ci = 0
    wl = []
    for j in range(len(pattern)):
        if pattern[j] == "*":
            if j - ci > 0:
                wl.append(pattern[ci:j])
            wl.append("*")
            ci = j+1
            continue
        elif pattern[j] == "?":
            if j - ci > 0:
                wl.append(pattern[ci:j])
            wl.append("?")
            ci = j+1
            continue
        elif j == len(pattern)-1:
            wl.append(pattern[ci:j+1])
    print(wl, match)
    if wild_card_rec(0, wl, 0, match):
        print(match)


def executor():
    input_list = util.readInput("wild_card.txt")
    i = 1
    while i < len(input_list):
        pattern = input_list[i][0]
        n = int(input_list[i+1][0])
        il = input_list[i+2:i+2+n]
        print(n, pattern, il)
        for s in il:
            wild_card(pattern, s[0])

        i += n+2


if __name__ == '__main__':
    executor()
