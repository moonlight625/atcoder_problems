from collections import deque

n,qn = map(int, input().split())
b = list(map(int, input().split()))
balls = [(a, i) for i, a in enumerate(b,1)]
balls.sort()

for _ in range(qn):
    m = int(input())
    q = list(map(int, input().split()))
    
    #value: ボールに書いてある番号、index:なん番目にそのボールがあるか
    for ball_value, ball_index in balls:
        if ball_index not in q:
            print(ball_value)
            break