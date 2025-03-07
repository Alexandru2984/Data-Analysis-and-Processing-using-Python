from functools import reduce

vocale = "aeiouAEIOU"
input_string = "Salutare, ce mai faci?"
##Varianta 1
final_string = list(filter(lambda x: x not in vocale, input_string))

# print(reduce(lambda x,y: x if x not in vocale else not x , input_string))

res = "".join(final_string)
print(res)
##Varianta 2
def elimina_vocale(ch):
    return ch not in vocale

print("".join((filter(elimina_vocale, input_string))))
##Varianta 3
print("".join([ch for ch in input_string if ch not in vocale]))