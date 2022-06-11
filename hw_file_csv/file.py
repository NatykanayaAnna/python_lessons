file = open('notebook.csv', 'a')
file.close()
file = open('notebook.csv', 'r')
for row in file:
    print(row)
file.close()