def max_sequence(arr):

    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start_index = i
        else:
            current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
            start_index = temp_start_index
            end_index = i

    return max_sum

if __name__ == "__main__":
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_sequence([-2, -5, 6, -2, -3, 1, 5, -6]))    # 7
    print(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]))    # 7
    print(max_sequence([-2, -5, 6, -2, -3, 1, 6, -6]))    # 8
    print(max_sequence([-2, -5, 6, 2, -3, 1, 6, -6]))     # 12