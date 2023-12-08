def first_n_smallest(arr ,n):
    smaller_number = []
    final_list = []
    for number in range(n):
        smaller_number.append(sorted(arr)[number]) # encuentra los números pequeños
    for position in range(len(arr)): 
        if len(final_list) <= n - 1: # pone el limite de n
            if arr[position] in smaller_number: 
                final_list.append(arr[position]) # guarda el numero
                smaller_number.remove(arr[position]) # borra el numero en smaller_number
    return final_list