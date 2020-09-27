from time import sleep


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def countdown(seconds):
    if seconds == 0:
        return 0
    else:
        print(seconds)
        sleep(1)
        return countdown(seconds - 1)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_generator():
    yield 1
    x = 1
    y = 2
    while True:
        yield x
        x *= y
        y += 1


factorial_generator = factorial_generator()


def fib_generator():
    yield 0
    x = 1
    y = 0
    while True:
        yield x
        x += y
        y = x


fib_generator = fib_generator()


def iterate(n, fn):
    for i in range(n):
        next(fn)
    return next(fn)


print(iterate(5, factorial_generator))
print(iterate(0, fib_generator))
print(iterate(1, fib_generator))
print(iterate(2, fib_generator))
print(iterate(3, fib_generator))
print(iterate(4, fib_generator))

# for i in range(5):
#     next(factorial_generator)           # this works
#     # next(factorial_generator())       # this doesn't, most peculiarly indeed

# print(next(factorial_generator))         # works
# # print(next(factorial_generator()))    # doesn't
