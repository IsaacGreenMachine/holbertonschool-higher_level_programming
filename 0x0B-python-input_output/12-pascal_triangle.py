#!/usr/bin/python3
"module for pascal_triangle"


def pascal_triangle(n):
    "returns a 2d list of ints that are a pascal triangle of size n"
    triangle = []
    if n > 0:
        for i in range(n):
            triangle.append([])
            if i == 0:
                triangle[0].append(1)
            else:
                for j in range(i + 1):
                    num = 0
                    if i - 1 >= 0 and j - 1 >= 0:
                        try:
                            num += triangle[i-1][j-1]
                        except IndexError:
                            pass
                    if i - 1 >= 0 and j >= 0:
                        try:
                            num += triangle[i-1][j]
                        except IndexError:
                            pass
                    triangle[i].append(num)
    return triangle
