N = int(input())

point = []

for i in range(N):
    x, y = map(int, input().split())

    point.append([])
    point[i].append(x)
    point[i].append(y)

point.sort(key = lambda x:(x[0], x[1]))

for x, y, in point:
    print(x, y)