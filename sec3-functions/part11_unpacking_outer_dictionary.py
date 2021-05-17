dc = {
    1: (200, "Aman"),
    2: (120, "Monty"),
    3: (150, "Vineet")
}

for key in dc:
    uid, name = dc[key]
    print(f"Uid : {uid}, Name : {name}")
else:
    print("Unpacking of dictionary of tuples using for loop completed")