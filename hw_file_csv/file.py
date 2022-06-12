my_file = open('notebook.csv', 'a')
text = input("Enter your string:\n")
my_file.write(text)
my_file.close()
my_file = open('notebook.csv', 'r')
for row in my_file:
    print(row)
my_file.close()