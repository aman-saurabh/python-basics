# Example :- First write and then read operation.
# Pre-existing text in the file is as follows :
"""
This is pre-existing data in write-and-read-first file.This is second sentence of pre-existing data.
"""
f = open("files/write-and-read-first.txt", "w+")
f.write("\nThis is a simple text for testing purpose.")
print("First read : ", f.read())
# Above read operation won't read anything as in this case pointer is positioned to the end of the file -
# after performing write operation.And there is no text after that position.
# So to actually get the data, we have to reposition the pointer at the beginning of the file.
f.seek(0)
print("Second read : ", f.read())

"""
Note :-
If we perform read operation first then it will not produce any result and the operation will be useless
as the pre-existing data is deleted while opening the file itself
and in that case pointer will also remain at the same position(i.e at the beginning of the file)
So if we perform write operation after that, the flow will same as the above example
So omitting example for such scenario.
"""
