# A nested loop is a loop inside another loop.
matrix = [
    ["Catto", "Doggo", "Bears"],
    ["Tiger", 1233456, "Snake"],
    ["Dears", "Sloth", "Cowwu"]
]

print(matrix[1][1])                           # [a][b] where 'a' represents the number of row (n'th object).
                                              #          and 'b' represents the number of column (n'th object in specified item).
def pen():
    for i in matrix:                          # This For loop will print each content of the Nested Loop.
        for e in i:
            print(e)
    for i in matrix:                          # This For loop wil print the nested loop as it is.
        print(i)
pen()
