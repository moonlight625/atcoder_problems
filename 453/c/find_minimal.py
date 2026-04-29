import subprocess
import random

def brute_force(n, ls):
    best = 0
    best_mask = 0
    for mask in range(1 << n):
        x = 0.5
        count = 0
        for i in range(n):
            direction = 1 if (mask >> i) & 1 else -1
            new_x = x + direction * ls[i]
            if (x > 0 and new_x < 0) or (x < 0 and new_x > 0):
                count += 1
            x = new_x
        if count > best:
            best = count
            best_mask = mask
    return best, best_mask

def run_cpp(n, ls):
    input_str = f"{n}\n" + "\n".join(map(str, ls)) + "\n"
    result = subprocess.run(
        ["./c"],
        input=input_str,
        capture_output=True,
        text=True,
        cwd="/Users/akiko/fork/atcoder_problems/453/c"
    )
    return int(result.stdout.strip())

def trace_greedy(n, ls):
    x = 0.5
    c = 0
    moves = []
    for i in range(n):
        l = ls[i]
        ax_minus = abs(x - l)
        ax_plus  = abs(x + l)
        if ax_minus < ax_plus:
            direction = -1
            new_x = x - l
            crossed = (new_x < 0)
        elif ax_minus > ax_plus:
            direction = +1
            new_x = x + l
            crossed = (new_x > 0)
        else:
            moves.append((l, 0, x, x, False))
            continue
        if crossed:
            c += 1
        moves.append((l, direction, x, new_x, crossed))
        x = new_x
    return c, moves

# まず小さい入力で不一致を探す
print("=== 小さい入力で反例を探索 ===")
for trial in range(200000):
    n = random.randint(2, 8)
    ls = [random.randint(1, 100) for _ in range(n)]

    expected, best_mask = brute_force(n, ls)
    got = run_cpp(n, ls)

    if expected != got:
        print(f"反例発見: n={n}, ls={ls}")
        print(f"  BF最適={expected}, greedy={got}")

        # BF最適の手順
        moves_str = []
        for i in range(n):
            d = '+' if (best_mask >> i) & 1 else '-'
            moves_str.append(d + str(ls[i]))
        print(f"  BF最適手順: {' '.join(moves_str)}")

        # BFでトレース
        x = 0.5
        bf_trace = [x]
        c = 0
        for i in range(n):
            direction = 1 if (best_mask >> i) & 1 else -1
            new_x = x + direction * ls[i]
            if (x > 0 and new_x < 0) or (x < 0 and new_x > 0):
                c += 1
            x = new_x
            bf_trace.append(x)
        print(f"  BF座標列: {bf_trace}")

        # greedyトレース
        _, greedy_moves = trace_greedy(n, ls)
        print(f"  Greedy手順:")
        for l, d, old_x, new_x, crossed in greedy_moves:
            print(f"    l={l}, {'右' if d>0 else '左'}: {old_x} -> {new_x} {'(通過)' if crossed else ''}")
        break
