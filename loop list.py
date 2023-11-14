#looplist using for loop

looplist = ["loop1", "loop2", "loop3", "loop4"]
for x in looplist:
    print(x)
    
    
#using for loop range and len

for x in range(len(looplist)):
    print(x)  
    

# list comprehension

looplist = [1,2,3,4]
new_list = [x*2 for x in looplist]
print(new_list)   

# sort list

looplist = [3,2,1,4]
new_list = sorted(looplist)
print(new_list) 

# reverse list

looplist = [3,2,1,4]
new_list = looplist[::-1]
print(new_list)

# copy list

numlist = [3,2,1,4]
num2 = looplist.copy()
print(num2) 

# join list

numlist = [3,2,1,4]
num2 = numlist + [5,6,7]
print(num2) 

# pop list

numlist = [3,2,1,4]
num2 = numlist.pop()
print(num2) 

# remove list

numlist = [3,2,1,4]
num2 = numlist.remove(2)
print(num2) 

# clear list

numlist = [3,2,1,4]
num2 = numlist.clear()
print(num2)
          