# Create two sets, set1 and set2, with some common and some different elements. Then, perform the following operations on the sets and print the results:
set1 = {1,2,3}
set2 = {2,3,4}
#Union of sets
union_set = set1.union(set2)
print(union_set) #prints the union of set1 and set2
#Intersection of sets
intersection_set = set1.intersection(set2)
print(intersection_set) #prints the intersection of set1 and set2
#Difference of sets
difference_set = set1.difference(set2)
print(difference_set) #prints the difference of set1 and set2
#Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set) #prints the symmetric difference of set1 and set2
#Subset of sets
is_subset = set1.issubset(set2)
print(is_subset) #prints whether set1 is a subset of set2
#Superset of sets
is_superset = set1.issuperset(set2)
print(is_superset) #prints whether set1 is a superset of set2
#Disjoint of sets
is_disjoint = set1.isdisjoint(set2)
print(is_disjoint) #prints whether set1 and set2 are disjoint