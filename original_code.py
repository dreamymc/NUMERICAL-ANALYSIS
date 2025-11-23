import math

def f(t):
    return math.exp(-0.3*t) - 0.5

def fp(t):
    return -0.3 * math.exp(-0.3*t)

print("NEWTON'S METHOD — BATTERY DECAY")
t = float(input("Initial guess: "))
tol = 1e-5

while True:
    t_new = t - f(t)/fp(t)
    print(f"t = {t_new:.6f}")

    if abs(t_new - t) < tol:
        break
    t = t_new

print(f"Root found at t ≈ {t_new:.6f}")
