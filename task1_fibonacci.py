from typing import Callable, Dict


def caching_fibonacci() -> Callable[[int], int]:
    cache: Dict[int, int] = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0  # Якщо n <= 0, повернути 0
        if n == 1:
            return 1  # Якщо n == 1, повернути 1
        if n in cache:  # перевірка чи є n у cache
            return cache[n]  # Якщо n у cache, повернути cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(
            n - 2
        )  # рекурсивний розрахунок та запис у кеш
        return cache[n]

    return fibonacci  # замикання повертає функцію в якій є кеш


if __name__ == "__main__":
    fib = caching_fibonacci()
    print(fib(10))
    print(fib(15))
