my_set = {1,2,3,4,5,6}
print("Initial Set:", my_set)

# for adding the element in the set 
my_set.add(7)
print("Set after adding 7:", my_set)

# for Removing a element in the set 
my_set.remove(2)
print("Set after removing 2:", my_set)

# for discord the element in the set 
my_set.discard(3)
print("after discarding the element:",my_set)

#  for pop a element in the set 
my_set.pop()
print("after poping the element:",my_set)

another_set = {3,4,5,6,7,78,98,76}

print("Union:", my_set | another_set)  # or my_set.union(another_set)
print("Intersection:", my_set & another_set)  # or my_set.intersection(another_set)
print("Difference:", my_set - another_set)  # or my_set.difference(another_set)
print("Symmetric Difference:", my_set ^ another_set)  # or my_set.symmetric_difference(another_set)

#  for clear a set 
my_set.clear()
print("after clearing the set:",my_set)