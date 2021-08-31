import util


def rec_jump_game(n: int, il: list, p: list, x: int, y: int):
    if x == n-1 and y == n-1:
        return True
    if (x < 0 or y < 0 or x >= n or y >= n) or p[x][y]:
        return False
    p[x][y] = True
    if rec_jump_game(n, il, p, x+il[x][y], y):
        return True
    elif rec_jump_game(n, il, p, x, y+il[x][y]):
        return True
    return False


def jump_game(n: int, l: list):
    return rec_jump_game(n, l, [[False for _ in range(n)] for _ in range(n)], 0, 0)


def jump_game2(il: list, x, y):
    if x >= len(il) or y >= len(il):
        return False
    if x == len(il)-1 and y == len(il)-1:
        return True
    return jump_game2(il, x+il[x][y], y) or jump_game2(il, x, y+il[x][y])


def jump_game3(il: list, cache: list, x, y):
    if x >= len(il) or y >= len(il):
        return False
    if x == len(il)-1 and y == len(il)-1:
        return True
    if cache[x][y]:
        return False
    cache[x][y] = True
    return jump_game2(il, x+il[x][y], y) or jump_game2(il, x, y+il[x][y])


def executor():
    input_list = util.readInput("jump_game.txt")
    i = 1
    while i < len(input_list):
        n = int(input_list[i][0])
        l = [list(map(int, input_list[j])) for j in range(i+1, i+n+1)]
        print(n, l)
        print(jump_game(n, l))
        print(jump_game2(l, 0, 0))
        print(jump_game3(l, [[False for _ in range(n)] for _ in range(n)], 0, 0))
        i += n+1


if __name__ == '__main__':
    executor()
