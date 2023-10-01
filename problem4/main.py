def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes_grid(cols, rows, start):
    primes = []
    num = start
    res = ""
    
    while len(primes) < rows * cols:
        if num != start and is_prime(num):
            primes.append(num)
        num += 1
    two_d_array = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(primes[i * cols + j])
        res = res + ' '.join(map(str, row)) + "\n" 
    return res

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    print(generate_primes_grid(5, 2, 1))




# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def generate_primes_grid(cols, rows, start):
#     primes = []
#     num = start
#     res = ""
    
#     while len(primes) < rows * cols:
#         if num != start and is_prime(num):
#             primes.append(num)
#         num += 1
#     two_d_array = []
#     for i in range(rows):
#         row = []
#         for j in range(cols):
#             row.append(primes[i * cols + j])
#         res = res + ' '.join(map(str, row)) + "\n"
#     return res

# if __name__ == "__main__":
#     print(generate_primes_grid(2, 3, 13))
#     """
#     17 19
#     23 29
#     31 37
#     """
#     print(generate_primes_grid(5, 2, 1))
#     """
#     2  3  5  7 11
#     13 17 19 23 29
#     """