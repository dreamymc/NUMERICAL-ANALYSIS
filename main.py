import math

def f(t):  ## the model
    return math.exp(-0.3 * t) - 0.5  ## battery-decay function (mao ni ang atong function f(t))

def fp(t):  ## the derivative
    return -0.3 * math.exp(-0.3 * t)  ## derivative ni f(t) (gamit sa Newton)

def newton_root(t0, tol, max_iter=200, f_tol=1e-8):
    t = float(t0)

    ## Newton's Method iterations
    for i in range(1, max_iter + 1):
        f_val = f(t)
        fp_val = fp(t)

    ##safety check if zero or gamay kaayo ang derivative
        if abs(fp_val) < 1e-12:
            raise ZeroDivisionError(
                f"Derivative too small at iter {i}, t={t:.8f}. Try a different initial guess."
            )

        ##  newton's formula ni siya --> t_new = t - f(t)/f'(t).
        t_new = t - f_val / fp_val

        ## Absolute relative error |er| (mao ni ang stopping criteria nato)
        rel_error = abs((t_new - t) / t_new)

        ## Print sa values para makita nato ang iteration behavior
        print(
            f"Iter {i:02d}: t = {t:.8f}, f(t) = {f_val:.4e}, f'(t) = {fp_val:.4e}, "
            f"t_new = {t_new:.8f}, rel_error = {rel_error:.4e}"
        )

        ## ----- STOPPING CRITERIA -----
        ## mu-stop ta kung ang relative error mas gamay na sa gi input nga tolerance
        if rel_error < tol:
            print(f"Stopping because RELATIVE ERROR < tol at iteration {i}.")
            return t_new, i

        ## 2nd criteria kung gamay na kaayo ang value sa f(t) (duol na kaayo sa root)
        if abs(f(t_new)) < f_tol:
            print(f"Stopping because f(t) is near zero at iteration {i}.")
            return t_new, i

        t = t_new  ## update ang t (move to next iteration)

    ## kung dili pa gyud mo-converge after max_iter, mo-error
    raise RuntimeError(
        f"Didn't converge within {max_iter} iterations. Last t = {t:.8f}"
    )


if __name__ == "__main__":
    print("NEWTON'S METHOD — BATTERY DECAY (f(t) = e^(-0.3t) - 0.5)")

    try:
        t0 = float(input("Enter your initial guess (t0): "))  ## initial guess input
    except ValueError:
        print("Invalid initial guess; please enter a valid number.")
        raise SystemExit(1)

    try:
        tol = float(input("Tolerance (e.g. 1e-5 or 0.00001): "))  ## input tolerance
    except ValueError:
        print("Invalid tolerance; using default 1e-5")
        tol = 1e-5

    try:
        root, iters = newton_root(t0, tol, max_iter=200)  ## call sa Newton function
        print(f"\nRoot found at t ≈ {root:.6f} after {iters} iterations")
    except Exception as e:
        print("\nError:", e)
        raise SystemExit(1)

    # analytic solution para ma-compare ninyo
    analytic = math.log(2) / 0.3
    print(f"Analytic solution: t = ln(2)/0.3 ≈ {analytic:.6f}")
    print(f"Residual f(root) = {f(root):.4e}")
