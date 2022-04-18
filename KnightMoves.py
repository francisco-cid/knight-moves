class Square(object):
    def __init__(self, x, y, count):
        self.x = x
        self.y = y
        self.count = count
        self.previous = None
        self.alg = coord_alg([self.x, self.y])[0] + str(coord_alg([self.x, self.y])[1])


# translates ij coordinates to algebraic chess notation
def coord_alg(pos):
    pos[0] = chr(97 + pos[0])
    pos[1] = pos[1] + 1
    return pos


# translates algebraic chess notation to ij coordinates
def alg_coord(pos):
    pos[0] = ord(pos[0]) - 97
    pos[1] = pos[1] - 1
    return pos


def is_inside(pos):
    if (pos.x >= 0 and pos.x <= 7) and (pos.y >= 0 and pos.y <= 7):
        return True
    else:
        return False


def min_moves(k_pos, target):
    # all possible moves
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    queue = []
    board = [[False for i in range(8)] for j in range(8)]
    k_pos = Square(k_pos[0], k_pos[1], 0)
    board[k_pos.x][k_pos.y] = True
    queue.append(k_pos)
    while len(queue) > 0:
        v = queue.pop(0)
        if [v.x, v.y] == target:
            count = v.count
            path = []
            while v != None:
                path.append(v.alg)
                v = v.previous
            path.reverse()
            print(path)
            return count
        for i in range(8):
            w = Square(v.x + dx[i], v.y + dy[i], v.count + 1)
            w.previous = v
            if is_inside(w):
                if not board[w.x][w.y]:
                    board[w.x][w.y] = True
                    queue.append(w)


def main():
    k_pos = ['a', 1]
    target = ['e', 3]
    print(min_moves(alg_coord(k_pos), alg_coord(target)))


main()
