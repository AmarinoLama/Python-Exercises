def sort_animals(lst):
    return sorted(lst, key=lambda x: (x.number_of_legs, x.name))