def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """ 
    * ? Return simple interest.
    """
    return (principal * rate * time) / 100


def main():
    try:
        p = float(input("Enter Principal amount: "))
        if p < 0:
            print("Values cannot be negative.")
            return
        r = float(input("Enter Rate of interest: "))
        if r < 0:
            print("Values cannot be negative.")
            return
        t = float(input("Enter Time (in years): "))

        if t < 0:
            print("Values cannot be negative.")
            return
        si = calculate_simple_interest(p, r, t)

        print(f"\nSimple Interest = {si}")
        print(f"Total Amount = {p + si}")

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()
