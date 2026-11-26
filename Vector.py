import sympy as sp
# Define variables
x, y, z = sp.symbols('x y z')
# Define scalar field
f = x**2 + y**2 + z**2
# Define vector field
F = (x**2, y**2, z**2)
# Gradient
grad = sp.Matrix([
    sp.diff(f, x),
    sp.diff(f, y),
    sp.diff(f, z)
])
# Divergence
div = sp.diff(F[0], x) + sp.diff(F[1], y) + sp.diff(F[2], z)
# Curl
curl = (
    sp.diff(F[2], y) - sp.diff(F[1], z),
    sp.diff(F[0], z) - sp.diff(F[2], x),
    sp.diff(F[1], x) - sp.diff(F[0], y)
)
# Display results
print("Gradient:")
sp.pprint(grad)
print("Divergence:")
sp.pprint(div)
print("Curl:")
sp.pprint(curl)