# AP Multiplication Table

print(" "+ "_" * 15)

for i in range(0, 16):
    if i == 0:
        print("| x", end="")
    else:
        print(f"{i}", end="")