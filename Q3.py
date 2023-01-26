def pascal_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            import math
            print(int(math.comb(i, j)), end = " ")
        print()
