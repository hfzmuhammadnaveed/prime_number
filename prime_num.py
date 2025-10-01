def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_factors(number, limit=1000000000000000000000):
    """Efficiently print up to `limit` number of factors of the number."""
    print(f"Factors of {number} (up to {limit} shown):")
    factors = set()
    count = 0
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)
            count += 2  # since we add i and number//i
            if count >= limit:
                break
    for factor in sorted(factors):
        print(factor, end=" ")
    print()


while True:
    user_input = input("Enter a number (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting program. Goodbye!")
        break
    if user_input.isdigit():
        num = int(user_input)
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
        print_factors(num)
    else:
        print("Invalid input. Please enter a positive integer.")
