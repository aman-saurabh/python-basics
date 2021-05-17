# Example2 :- First write and then read operation.
# Pre-existing text in the file is as follows :
"""
This is pre-existing data in read-and-write-second file.This is second sentence of pre-existing data.
"""
f = open("files/read-and-write-second.txt", "r+")
print("Before first write pointer position : ", f.tell())
f.write("This is just a simple text for testing purpose.")
print("Before first read pointer position : ", f.tell())
print("First read : ", f.read())
# Above read operation won't read anything as in this case pointer is positioned to the end of the file -
# after performing write operation.And there is no text after that position.
# So to actually get the data, we have to reposition the pointer at the beginning of the file.
f.seek(0)
print("Second read : ", f.read())
# We will see the pre-existing text is over-ridden by the given text.
# And also note that, not all pre-existing text is deleted.
# Only that much text is deleted(overridden) which the given text can override.

# To avoid such unexpected situations we must have to reposition the pointer to the beginning of the file.
