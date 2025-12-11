import argparse
import sys
import numpy as np
import matplotlib.pyplot as plt


def parse_exponent(s: str):
    try:
        return float(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f"invalid exponent: {s}")

def main():
    p = argparse.ArgumentParser(description="Plot y = x^n")
    p.add_argument("-n", "--exponent", type=parse_exponent, help="exponent n (e.g. 3 or 0.5)")
    p.add_argument(
        "--xmax",
        type=float,
        default=2.0,
        help="maximum absolute x to plot (default 2.0). For non-integer exponents x>=0 is used.",
    )
    p.add_argument("--points", type=int, default=400, help="number of sample points")
    p.add_argument("--save", action="store_true", help="save plot as x_pow_n.png")
    args = p.parse_args()
    if args.exponent is None:
        try:
            s = input("Enter exponent n (e.g. 3 or 0.5): ").strip()
        except (EOFError, KeyboardInterrupt):
            sys.exit(0)
        try:
            n = parse_exponent(s)
        except argparse.ArgumentTypeError as e:
            print(e)
            sys.exit(1)
    else:
        n = args.exponent

    is_int = float(n).is_integer()
    xmax = max(0.1, args.xmax)

    if is_int:
        x = np.linspace(-xmax, xmax, args.points)
        y = np.power(x, int(n))
    else:
        x = np.linspace(0.0, xmax, args.points)
        y = np.power(x, n)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, lw=2)
    plt.axhline(0, color="#444", lw=0.7)
    plt.axvline(0, color="#444", lw=0.7)
    plt.grid(True, alpha=0.4)
    plt.title(f"y = x^{n}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    if args.save:
        fname = f"x_pow_{str(n).replace('.', '_')}.png"
        plt.savefig(fname, dpi=150)
        print(f"Saved plot to {fname}")

    plt.show()


if __name__ == "__main__":
    main()