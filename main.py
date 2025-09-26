def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)  # возвращаем модуль, чтобы обработать отрицательные числа