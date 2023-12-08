def how_many_days(month):
    day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    return day_in_month[month - 1]

def test():
    assert how_many_days(1) == 31
    assert how_many_days(9) == 30
    assert how_many_days(2) == 28
    return "All tests finished"

print(test())