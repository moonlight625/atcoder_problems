height, width,qn = map(int, input().split())

for _ in range(qn):
    type, x = map(int, input().split())
    if type == 1:
        print(x * width)
        height -= x
    elif type == 2:
        print(x * height)
        width -= x