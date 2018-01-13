# investment tracker 1.0


def invest(amount, rate, time):
    year = 0

    print(f"principal amount: ${amount}")
    print(f"annual rate of return: {rate}%")

    for x in range(1, time + 1):
        year += 1
        increase = amount * rate
        amount = amount + increase
        print(f"Year {year}: ${amount}")
    print()


invest(100, .05, 8)
invest(2000, .025, 5)
