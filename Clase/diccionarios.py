population = {"Shangai":17.8, "Istanbul":13.3, "Karachi":13.0, "Mumbai":12.5}
print(population["Mumbai"])
print("----------------------------------")

#* lo siguente es como un .append en listas

population["fornelos"] = "yo" 
print(population)
print("----------------------------------")

# diccionarios dentro de diccionarios

population["galicia"] = {"pontevedra":100, "Ourense":1434, "Coruña":1212, "Lugo":444}
print(population)
print(population["galicia"]["pontevedra"])
print("----------------------------------")

# lista printeada con un for

for position in population:
    print(position)
    print(population[position])
print("----------------------------------")

#* compresiones con diccionarios

table = {'Holy Grail': '1975','Life of Brian': '1979','The Meaning of Life': '1983'}

d = list(table.items())
e = [title for (title, year) in table.items() if year == '1975']

print(d)
print(e)

print("..........................................")

D = {x: x ** 2 for x in [1, 2, 3, 4]}
print(D)
D = {c: c * 4 for c in 'SPAM'}
print(D)
D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print(D)
D = dict.fromkeys(['a', 'b', 'c'], 0)
print(D)
D = {k:0 for k in ['a', 'b', 'c']}
print(D)
D = dict.fromkeys('spam')
print(D)
D = {k: None for k in 'spam'}
print(D)