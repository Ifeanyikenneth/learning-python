print("Treasure Hunt")
row1 = ["💌", "💌", "💌"]
row2 = ["💌", "💌", "💌"]
row3 = ["💌", "💌", "💌"]

map = [row1, row2, row3]
print(f"{row1}\n {row2}\n {row3}")

position = input("where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

final = map[vertical- 1]
final[horizontal - 1] = "X"

print(final)


