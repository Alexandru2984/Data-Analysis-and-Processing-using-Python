
lista = [10,2,30,50,300,10]

#Filter + functie lambda
print(list(filter(lambda x: x> 5, lista)))

#List comprehension
print([element for element in lista if element > 5])