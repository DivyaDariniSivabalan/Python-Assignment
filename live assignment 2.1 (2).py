l=[1,2,3,4,5]
#append() Adds an element at the end of the list#
l.append(6)
print(l)
#copy() Returns a copy of the list#
l.copy()
print(l)
#count() Returns the number of elements with the specified value#
x=l.count(1)
print(x)
#extend() Add the elements of a list (or any iterable), to the end of the current list#
l1=[7,8,9,10,11]
l.extend(l1)
print(l)
#index() Returns the index of the first element with the specified value#
y=l.index(3)
print(y)
#insert() Adds an element at the specified position#
l.insert(2,12)
print(l)
#pop() Removes the element at the specified position#
l.pop(3)
print(l)
#remove() Removes the item with the specified value#
l.remove(5)
print(l)
#reverse() Reverses the order of the list#
l.reverse()
print(l)
#sort() Sorts the list#
l.sort()
print(l)
#clear() Removes all the elements from the list#
l.clear()
print(l)
