# Read theory part from the online document before executing these file-handling programs.
f = open('files/my_file.txt', 'w+')
print("Pointer position in the beginning - ", f.tell())
f.write("Hello World!")
print("Pointer position after performing write operation - ", f.tell())
print("Text after repositioning it - ", f.read())       # Read1
f.seek(0)
print("Pointer position after repositioning it - ", f.tell())
print("Text after repositioning it - ", f.read())       # Read2
print(type(f))
"""
Here you will see it printed nothing in 'Read1' but printed "Hello World!" in Read2.
Even though we had performed write operation before Read1 and we haven't performed any write operation after Read1.
So, why it printed nothing in 'Read1' but printed "Hello World!" in Read2?
Actually it is because of the pointer position. Since in Read1, the pointer was at the end of the file
i.e in Read1 pointer was after "Hello World!" text, 
so when we performed read operation, it starts reading from the position it was currently and not from the beginning.
Since no text was there after the current pointer position, so it read nothing.
But in case of Read2 since we had repositioned it at the beginning of the file, 
So it read the text we had written i.e "Hello World!"
"""
