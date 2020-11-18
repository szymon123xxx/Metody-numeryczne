from scipy import optimize


def f(x):
    return (2*x**4 + 24*x**3 + 61*x**2 - 16*x + 1)


root1 = optimize.ridder(f, -9, -7)
root2 = optimize.ridder(f, -8, -4)
root3 = optimize.ridder(f, -1, 0.122320344)
root4 = optimize.ridder(f, 0.122805626, 1)

print(root1)
print(root2)
print(root3)
print(root4)
