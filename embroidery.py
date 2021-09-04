def draw_rectangle(width, height, fill_color='2', border_width=2, border_color='1'):
    matrix = []
    for i in range(width):
        matrix.append([])
        for j in range(height):
            matrix[i].append(fill_color)

    for i in range(border_width):
        for r in range(width):
            matrix[r][i] = border_color  # rift
            matrix[i][r - 1] = border_color  # up
    for i in range(height - border_width, height):
        for l in range(height):
            matrix[l][i] = border_color  # left
            matrix[i+1][l] = border_color  # down

    for line in matrix:
        print(*line)


print(draw_rectangle(10, 9))


def draw_triangle(height):
    matrix = []
    return matrix


def draw_christmas_tree(blocks):
    matrix = []
    return matrix


def draw_circle(radius):
    matrix = []
    return matrix


def embroider(matrix, color_scheme):
    for row in matrix:
        for cell in row:
            print(color_scheme[cell], end='')
        print()
    print()


if __name__ == '__main__':
    color_scheme = {0: ' ', 1: '*', 2: '.'}
    embroider([[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 2, 1, 0, 0], [
              0, 1, 2, 2, 2, 1, 0], [1, 1, 1, 1, 1, 1, 1]], color_scheme)
