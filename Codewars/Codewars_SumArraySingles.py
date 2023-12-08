def repeats(arr):
    num_no_rep = []
    for number in arr:
        if arr.count(number) == 2:
            continue
        else:
            num_no_rep.append(number)
    return sum(num_no_rep)