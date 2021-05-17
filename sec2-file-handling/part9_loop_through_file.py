print("Loop through file opened using open() method.")
file = open("files/with-statement-demo.txt")
for line in file:
    print(line)
file.close()

print("*********************************************************************************")

print("Loop through file opened using with statement.")
with open("files/with-statement-demo.txt", "rt") as f:
    for line in f:
        print(line)

