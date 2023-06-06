def fibo(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + 1
    return a