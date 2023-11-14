import re
text = "The rain in spain"
pattern = "[a-z]"
a = re.findall(pattern, text)
print(a)

#start with

text = "1 The rain in spain"
pattern = "^1"
a = re.findall(pattern, text)

if a:
    print("yes", 1 is not None)
else:
    print("no", 1 is None)    
    
