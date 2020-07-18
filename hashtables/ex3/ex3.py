def intersection(arrays):
    """
    YOUR CODE HERE
    """
    all_arrays = len(arrays)
    number_cache = {}
    result = []

    for array in arrays:
        for num in array:
            if num not in number_cache:
                number_cache[num] = 1
            else:
                number_cache[num] += 1
                if number_cache[num] == all_arrays:
                    result.append(num)

    
    # Your code here

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
