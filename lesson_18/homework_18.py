from __future__ import annotations
from typing import Iterable, Iterator, Callable, TypeVar, Any
from functools import wraps

T = TypeVar("T")
R = TypeVar("R")


# ========================= Генераторы =========================

def all_gen(n: int) -> Iterator[int]:
    for x in range(0, n + 1, 2):
        yield x


def fib_gen(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b



# ========================= Итераторы =========================

class ReverseListIterator(Iterator[T]):
    def __init__(self, items: list[T]):
        self._items = items
        self._i = len(items) - 1

    def __iter__(self) -> "ReverseListIterator[T]":
        return self

    def __next__(self) -> T:
        if self._i < 0:
            raise StopIteration
        val = self._items[self._i]
        self._i -= 1
        return val


class AllRangeIterator(Iterator[int]):
    def __init__(self, n: int):
        self._n = n
        self._cur = 0

    def __iter__(self) -> "AllRangeIterator":
        return self

    def __next__(self) -> int:
        if self._cur > self._n:
            raise StopIteration
        val = self._cur
        self._cur += 2
        return val



# ========================= Декораторы =========================

def log_call(fn: Callable[..., R]) -> Callable[..., R]:
    @wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> R:
        print(f"[LOG] {fn.__name__} args={args}, kwargs={kwargs}")
        res = fn(*args, **kwargs)
        print(f"[LOG] {fn.__name__} result={res}")
        return res
    return wrapper


def catch_exceptions(
    default: R | None = None,
    exceptions: tuple[type[BaseException], ...] = (Exception,),
) -> Callable[[Callable[..., R]], Callable[..., R | None]]:
    def deco(fn: Callable[..., R]) -> Callable[..., R | None]:
        @wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> R | None:
            try:
                return fn(*args, **kwargs)
            except exceptions as e:
                print(f"[ERROR] {fn.__name__}: {type(e).__name__}: {e}")
                return default
        return wrapper
    return deco



# ========================= Мини Тестик Использования =========================

if __name__ == "__main__":
    print("\n=== Генераторы ===")
    print("Генератор Парных:", list(all_gen(10)))
    print("Генератор Фибоначчи:", list(fib_gen(30)))

    print("\n=== Итераторы ===")
    data = [1, 2, 3, 4]
    print("Итератор Обратных:", list(ReverseListIterator(data)))
    print("Итератор Парных:", list(AllRangeIterator(10)))

    print("\n=== Декораторы ===")
    @log_call
    def add(a: int, b: int) -> int:
        return a + b
    add(2, 5)

    @catch_exceptions(default="fallback")
    def div(a: float, b: float) -> float:
        return a / b

    print("div(10, 2):", div(10, 2))
    print("div(10, 0):", div(10, 0))