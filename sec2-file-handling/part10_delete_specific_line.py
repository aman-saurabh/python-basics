"""
This is the first line of file delete-line-demo.
This is its second line
This is the line we want to remove.
This is the last line of the file and it should not be removed.
"""
with open("files/delete-line-demo.txt", "r+") as f:
    lines = f.readlines()
    f.seek(0)
    for line in lines:
        if line.strip("\n") != "This is the line we want to remove.":
            f.write(line)
    f.truncate()
    f.seek(0)
    print(f.read())
