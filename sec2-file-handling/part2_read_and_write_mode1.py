# Example1 :- First read and then write operation.
# Pre-existing text in the file is as follows :
"""
This is pre-existing data in read-and-write-first file.This is second sentence of pre-existing data.
"""
f = open("files/read-and-write-first.txt", "r+")
print("Before first read pointer position : ", f.tell())
print("First Read : ", f.read())
print("Before first write pointer position : ", f.tell())
f.write("\nThis is just a simple text for testing write operation.")
print("Before second read pointer position : ", f.tell())
print("Second read : ", f.read())
# Above read operation won't read anything as in this case pointer is positioned to the end of the file -
# after performing write operation.And there is no text after that position.
# So to actually get the data, we have to reposition the pointer at the beginning of the file.
f.seek(0)
print("Third read : ", f.read())
f.close()

