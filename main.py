name = input("please enter your name: ")
print("welcome", name)
libraries = []
count = int(input("how many books do you want? "))
for i in range(count):
    library = input("plaese enter a library name: ")
    libraries.append(library)
print("your libraries name: ", libraries )