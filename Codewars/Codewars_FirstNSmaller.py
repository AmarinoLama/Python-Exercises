def first_n_smallest(arr ,n):
    smaller_number = []
    final_list = []
    for number in range(n):
        smaller_number.append(sorted(arr)[number])
    for position in range(len(arr)):
        if len(final_list) <= n - 1:
            if arr[position] in smaller_number:
                final_list.append(arr[position])
                smaller_number.remove(arr[position])
    return final_list