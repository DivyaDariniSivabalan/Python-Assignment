d={}
#copy()	Returns a copy of the dictionary#
car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.copy()
print(x)
#fromkeys() Returns a dictionary with the specified keys and value#
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)
#get() Returns the value of the specified key#
z=car.get("model")
print(z)
#items() Returns a list containing a tuple for each key value pair#
k=car.items()
print(k)
#keys()	Returns a list containing the dictionary's keys#
p=car.keys()
print(p)
#pop() Removes the element with the specified key#
c=car.pop("model")
print(c)
#popitem() Removes the last inserted key-value pair#
l=car.popitem()
print(l)
#setdefault() Returns the value of the specified key. If the key does not exist: insert the key, with the specified value#
q = car.setdefault("model", "Bronco")
print(q)
#update() Updates the dictionary with the specified key-value pairs#
car.update({"color": "White"})
print(car)
#clear() Removes all the elements from the dictionary#
car.clear()
print(car)
#values() Returns a list of all the values in the dictionary#
a = car.values()
print(a)

