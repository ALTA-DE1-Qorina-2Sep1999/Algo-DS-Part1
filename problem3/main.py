def fibonacci(number):
    x = 0
    y = 1
    count = 0 

    if number <= 0:
        return 0
    for i in range(0, number):
        x = y
        y = count
        count = x + y
    return count

if __name__ == "__main__":
    print(fibonacci(0))  # 0
    print(fibonacci(2))  # 1
    print(fibonacci(9))  # 34
    print(fibonacci(10)) # 55
    print(fibonacci(12)) # 144