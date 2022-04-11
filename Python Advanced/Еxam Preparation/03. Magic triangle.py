def get_magic_triangle(n):
    triangle = []
    for r in range(n):
        triangle.append([0] * (1+r))
    triangle[0][0] = 1
    for r in range(n):
        for c in range(len(triangle[r])):
            if 0 <= r - 1 < len(triangle[r-1]) and 0 <= c - 1 < len(triangle[r-1]):
                triangle[r][c] += triangle[r - 1][c - 1]
            if 0 <= r - 1 < len(triangle[r - 1]) and 0 <= c < len(triangle[r - 1]):
                triangle[r][c] += triangle[r - 1][c]

    return triangle


print(get_magic_triangle(5))