# python sets

set1 = {1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set1)


# access set items

set1 = {1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
for i in set1:
    print(i)
    print(3 in set1)
    
    
# add set items

set1 = {1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set1.add(11)
set1.add(12)
set1.add(13)
set1.add(14)
print(set1)

# update set items

set1 = {1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set1.update([11, 12, 13, 14])
print(set1)

# remove set items

set1 = {1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set1.remove(1)
set1.remove(2)
set1.remove(3)
set1.remove(4)
print(set1)


# loop sets

set1 = {1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
for i in set1:
    print(i)


# join sets

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
set3 = set1.union(set2)
print(set3) 