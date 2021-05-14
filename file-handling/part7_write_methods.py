f = open("files/write_methods_file.txt", "w+t")
f.write("This is single statement written using write() method.")
f.write("\n\n")
# To add a line gap between above and below statements.
f.write("These are multiple statements.\nThese statements are also written using write() methods.")
f.write("\n\n")
# To add a line gap between above and below statements.
str_list = ["This is first statement of the list.",
            "This is second statement of the list.",
            "\nThis is third statement of the list written in a new line."]
f.writelines(str_list)
f.seek(0)
print(f.read())
