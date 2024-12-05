import functools
import itertools


def main():
    word_search =[]
    with open('input') as f:
        for line in f.readlines():
            word_search.append(list(line.strip()))

    total = 0
    word = tuple("XMAS")
    rows = len(word_search)
    cols = len(word_search[0])


    directions = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
    directions.remove((0,0))

    # part 1
    def is_xmas(i,j,direction, w):
        dr,dc = direction
        if len(w)==1 and word_search[i][j] == w[0]:
            return True
        if word_search[i][j] != w[0]:
            return False
        if i+dr < 0 or i+dr >= rows:
            return False
        if j+dc < 0 or j+dc >= cols:
            return False
        return is_xmas(i + dr, j + dc, direction, w[1:])

    for i in range(rows):
        for j in range(cols):
            for d in directions:
                if is_xmas(i, j, d, word):
                    total += 1

    print(f"Part 1: {total}")

    # part 2
    total = 0
    def is_x_mas(i, j):
        if word_search[i][j] != "A":
            return False
        diags = ((1,1),(1,-1))
        def is_mas(d):
            dr,dc = d
            if (((i + dr < 0 or i + dr >= rows or
                    j + dc < 0 or j + dc >= cols) or
                    i - dr < 0 or i - dr >= rows) or
                    j - dc < 0 or j - dc >= cols):
                return False
            dstr="".join([word_search[i+dc][j+dr], word_search[i-dc][j-dr]])
            return dstr == "MS" or dstr == "SM"
        return all(is_mas(d) for d in diags)

    for i in range(rows):
        for j in range(cols):
            if is_x_mas(i, j):
                total += 1

    print(f"Part 2: {total}")

if __name__ == '__main__':
    main()