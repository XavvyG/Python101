def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x):
            if (x % n == 0):
                return False
            return True

print(is_prime(10))