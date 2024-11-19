m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

max_sum = m + n - 1
for sum in range(max_sum):
    for i in range(sum):
        if i < m and sum - i < n:
            print(matrix[i][sum - i], end=" ")
    print()
