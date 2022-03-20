def mandelbrot(number, c):
    if number == 0:
        return 0

    return mandelbrot(number - 1, c) ** 2 + c


def sequence(c):
    seq = 0
    while True:
        yield seq
        seq = seq ** 2 + c


for n in range(10):
    print(f"mandelbrot({n}) = {mandelbrot(n, c=1)}")


# More efficient way to calculate the sequence
for n, z in enumerate(sequence(c=1)):
    print(f"mandelbrot({n}) = {z}")
    if n >= 9:
        break
