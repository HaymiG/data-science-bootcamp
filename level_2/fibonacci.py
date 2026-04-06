def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

print(fibonacci(6))  # [0, 1, 1, 2, 3, 5]

