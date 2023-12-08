def find_second(a,b):
    first_find = a.find(b)
    return a.find(b,first_find + 1)

#Estas variables para que no sea confuso deberían tener un nombre distinto al del def
a = "hoy es un dia muy importante ya que hoy es la boda de Maria"
b = "hoy"

print(find_second(a,b))