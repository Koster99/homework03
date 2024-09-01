import time
from multiprocessing import Pool, cpu_count

def factorize_number(n):
    """
    Повертає список усіх дільників числа n.
    """
    return [i for i in range(1, n + 1) if n % i == 0]

def factorize(*numbers):
    """
    Синхронна версія функції факторизації.
    """
    return [factorize_number(n) for n in numbers]

def factorize_parallel(*numbers):
    """
    Паралельна версія функції факторизації з використанням багатопроцесорності.
    """
    with Pool(cpu_count()) as pool:
        return pool.map(factorize_number, numbers)

if __name__ == "__main__":
    # Перевірка роботи функції
    numbers = [128, 255, 99999, 10651060]

    # Синхронна версія
    start_time = time.time()
    results_sync = factorize(*numbers)
    sync_duration = time.time() - start_time

    # Паралельна версія
    start_time = time.time()
    results_parallel = factorize_parallel(*numbers)
    parallel_duration = time.time() - start_time

    # Вивід результатів
    print(f"Синхронна версія зайняла: {sync_duration:.4f} секунд")
    print(f"Паралельна версія зайняла: {parallel_duration:.4f} секунд")

    # Перевірка правильності
    assert results_sync == results_parallel
