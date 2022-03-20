def z(n, c):
    if n == 0:
        return 0

    return z(n - 1, c) ** 2 + c


for n in range(10):
    print(f"z({n}) = {z(n, c=1)}")
