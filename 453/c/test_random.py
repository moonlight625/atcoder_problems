import subprocess
import random

def brute_force(n, ls):
    """全探索: 2^n 通りの符号の組み合わせを試す"""
    best = 0
    for mask in range(1 << n):
        x = 0.5
        count = 0
        for i in range(n):
            direction = 1 if (mask >> i) & 1 else -1
            new_x = x + direction * ls[i]
            if (x > 0 and new_x < 0) or (x < 0 and new_x > 0):
                count += 1
            x = new_x
        best = max(best, count)
    return best

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

errors = 0
total = 5000

for test_num in range(total):
    n = random.randint(1, 15)  # 2^15=32768 で全探索可能
    ls = [random.randint(1, 10**9) for _ in range(n)]

    expected = brute_force(n, ls)
    got = run_cpp(n, ls)

    if expected != got:
        print(f"[MISMATCH] n={n}, ls={ls}")
        print(f"  expected={expected}, got={got}")
        errors += 1
        if errors >= 10:
            print("10件以上の不一致が見つかったため中断")
            break

if errors == 0:
    print(f"全 {total} ケースでBFと一致（潜在バグなし）")
else:
    print(f"{total} ケース中 {errors} 件の不一致")
