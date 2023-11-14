file1 = open("Textfile.txt", "r")


print(file1.read())

# write file to file

file2 = open("Textfile.txt", "w")

file2.write("Hello World")

file3 = open("Textfile.html", "w")

file3.write("<h1>Hello World</h1>")

file2.close()

#delete file

import os
os.remove("Textfile.html")

