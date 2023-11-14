# tuple

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tup)
print(type(tup))

# update tuple

tup = tup + (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
print(tup)
print(type(tup))

# unpack tuple

tup = ('a'," b",' c', 'd',' e',' f', 'g',' h',' i',' j ')
(*a,b,c) = tup
print(b)

# loop tuple

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in tup:
    print(i)
    
for x in range(len(tup)):
    print(tup[x])   

# while loop tuple

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
i = 0
while i < len(tup):
    print(tup[i])
    i += 1     
    
# join tuple

tup1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tup2 = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
tup = tup1 + tup2
print(tup)    


# tuple methods

num = (1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10)
x = num.count(5)
print(x)
