# Example :- First write and then read operation.
# Pre-existing text in the file is as follows :
"""
This is pre-existing data in write-and-read-first file.This is second sentence of pre-existing data.
"""
f = open("files/append-and-write-first.txt", "a+")
print("Pointer position before performing first write operation : ", f.tell())
f.write("\nThis is a simple text for testing purpose.")
print("First read : ", f.read())
# Above read operation won't read anything as in this case pointer is positioned to the end of the file -
# after performing write operation.And there is no text after that position.
# So to actually get the data, we have to reposition the pointer at the beginning of the file.
f.seek(0)
print("Second read : ", f.read())
# Now let's again reposition the pointer at the beginning of the file and again perform write operation
# And let's see whether it over-ride the existing text or
# append the new text after the existing text.
f.seek(0)
f.write("\nThis is second text for testing purpose.")
# Now again perform read operation
f.seek(0)
print("Third read : ", f.read())
