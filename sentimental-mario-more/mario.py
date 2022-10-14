import cs50

height = 0

while height <= 0 or height > 8:
    height = cs50.get_int("height: ")

for i in range(height):
    row = height - 1
    for j in range(height):
        if i >= row:
            print("#", end="")
        else:
            print(" ", end="")
        row -= 1
    print("  " + ((i + 1) * ("#")))
