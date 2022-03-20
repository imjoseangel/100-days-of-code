def sequence(c, seq=0):
    while True:
        yield seq
        seq = seq ** 2 + c


def mandelbrot(candidate):
    return sequence(seq=0, c=candidate)


def julia(candidate, parameter):
    return sequence(seq=candidate, c=parameter)


for n, z in enumerate(sequence(c=1)):
    print(f"mandelbrot({n}) = {z}")
    if n >= 9:
        break
