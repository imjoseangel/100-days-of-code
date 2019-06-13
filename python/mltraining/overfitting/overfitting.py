import matplotlib.pyplot as plt


def real_funct(x):
    return [-(i**2) for i in x]


def over_funct(x):
    return [-0.5 * (i**3) - (i**2) for i in x]


def under_funct(x):
    return [6 * i + 9 for i in x]


# create x values, and run them through each function
current_x = range(-3, 4, 1)
real_y = real_funct(current_x)
over_y = over_funct(current_x)
under_y = under_funct(current_x)

# Use matplotlib to plot the functions so they can be visually compared.
plt.plot(current_x, real_y, 'k', label='Real function')
plt.plot(current_x, over_y, 'r', label='Overfit function')
plt.plot(current_x, under_y, 'b', label='Underfit function')
plt.legend()
plt.show()

# Output the data in a well formatted way, for the more numerically inclined.
print("An underfit model may output something like this:")
for i in range(0, 7):
    print("x: " + str(current_x[i]) + ", real y: " + str(real_y[i]) + ", y: " +
          str(under_y[i]))

print("An overfit model may look a little like this")
for i in range(0, 7):
    print("x: " + str(current_x[i]) + ", real y: " + str(real_y[i]) + ", y: " +
          str(over_y[i]))
