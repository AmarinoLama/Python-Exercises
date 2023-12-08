def loose_change(cents):
    myCoins = {'Pennies':0, 'Nickels':0, 'Dimes':0, 'Quarters':0}
    if cents <= 0:
        return myCoins
    myCoins['Quarters'] = cents // 25
    cents = cents % 25
    myCoins['Dimes'] = cents // 10
    cents = cents % 10
    myCoins['Nickels'] = cents // 5
    cents = cents % 5
    myCoins['Pennies'] = cents // 1
    return myCoins