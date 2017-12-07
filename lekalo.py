import json
LIST_OF_CAM = {
    "Дима": {0:"XXS", 1:"XS", 2:"S", 3:"M", 4:"L", 5:"XL", 6:"XXL", 7:"XXXL", 8:"4XL"},
    "Катя": {0:"XXS", 1:"XS", 2:"S", 3:"M", 4:"L", 5:"XL", 6:"XXL", 7:"XXXL", 8:"4XL"},
    "Маша": {0:"XXS", 1:"XS", 2:"S", 3:"M", 4:"L", 5:"XL", 6:"XXL", 7:"XXXL", 8:"4XL"},
}

# возвращает список [['Дима', 'Дима'], ['Катя', 'Катя'], ['Маша', 'Маша']]
def camlist(loc): # превращаем множество лекал в список для модели в choice
    camlist = []
    for name in loc:
        double = []
        double.append(name)
        double.append(name)
        camlist.append(double)
    return camlist

l = camlist(LIST_OF_CAM)
print(l)

# возвращает список [['XXS', 0], ['XS', 0], ['S', 0], ['M', 0], ['L', 0]]
def lset(loc, camname):
    i = 0
    lset = []
    while i < len(loc[camname]):
        l = []
        l.append(loc[camname][i])
        l.append(0)
        lset.append(l)
        i += 1
    return lset

p = lset(LIST_OF_CAM, 'Дима')
print(p)

p = json.dumps(p)
print(p)

