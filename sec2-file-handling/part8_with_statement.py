with open("files/with-statement-demo.txt", "r+") as f:
    print("Pointer position before read operation : ", f.tell())
    print("First read : ", f.read())
    print()
    print("Pointer position before write operation : ", f.tell())
    f.write("\nThis line is added using write() method.")
    print("Pointer position after write operation : ", f.tell())
    print()
    f.seek(0)
    print("Second read : ", f.read())
    # No need to calling close() method as 'with statement' implicitly does it for us.
