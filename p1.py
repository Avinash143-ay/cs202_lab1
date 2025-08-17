"""Module to perform basic math operations and check prime numbers."""

class Calculator:
    """Performs basic arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Return the sum of two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Return the difference between two numbers."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Return the product of two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Return the division of two numbers. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


def is_prime(number: int) -> bool:
    """Check if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def prime_numbers_up_to(limit: int) -> list[int]:
    """Return a list of prime numbers up to the given limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def main() -> None:
    """Main function to demonstrate calculator and prime number utilities."""
    calc = Calculator()
    print("Addition of 5 + 3:", calc.add(5, 3))
    print("Subtraction of 5 - 3:", calc.subtract(5, 3))
    print("Multiplication of 5 * 3:", calc.multiply(5, 3))
    print("Division of 5 / 3:", calc.divide(5, 3))
    limit = 20
    primes = prime_numbers_up_to(limit)
    print(f"Prime numbers up to {limit}:", primes)


if __name__ == "__main__":
    main()
