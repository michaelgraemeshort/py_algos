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


def factorial_g():
    yield 1
    n = 1
    factorial_of_n_minus_one = 1
    while True:
        result = n * factorial_of_n_minus_one
        yield result
        n += 1
        factorial_of_n_minus_one = result


def fibonacci_g():
    yield 0
    yield 1
    n_minus_two = 0
    n_minus_one = 1
    while True:
        n = n_minus_two + n_minus_one
        yield n
        n_minus_two = n_minus_one
        n_minus_one = n


def return_nth_iteration(n, fn):
    fn = fn()
    for i in range(n):
        next(fn)
    return next(fn)


# next(fibonacci_g()) just keeps returning 0
# but if you assign fibonacci_g() to a variable e.g. spam, next(spam) iterates as expected

# hofstadter's q sequence: not suitable for this approach
# need to keep all of the q values up to Q(n), not just the last two, as far as I can tell
