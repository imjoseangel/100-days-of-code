import matplotlib.pyplot as plt
import numpy as np

np.warnings.filterwarnings("ignore")


def is_stable(candidate, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + candidate
    return abs(z) <= 2


def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j


def get_members(candidate, num_iterations):
    mask = is_stable(candidate, num_iterations)
    return candidate[mask]


c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=21)
members = get_members(c, num_iterations=20)

plt.scatter(members.real, members.imag, color="black", marker=",", s=1)
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()
