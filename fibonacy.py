def fib(n):
    if n < 0:
        raise("The number should be greater than 0")
    if n == 0 or n == 1:
        return 1

    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    print(fib(10))
