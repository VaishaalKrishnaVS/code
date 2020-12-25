row1 = ["❤️", "❤️", "❤️"]
row2 = ["❤️", "❤️", "❤️"]
row3 = ["❤️", "❤️", "❤️"]

row = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

a = input("which place do you want to replace with X\n")

horizontal = int(a[0])
vertical = int(a[1])

selected_row = row[vertical - 1]
selected_row[horizontal - 1] = "X"

# this can alsobe used
#row[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
