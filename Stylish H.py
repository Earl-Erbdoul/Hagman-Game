h = 'H'
# top right cone
for row in range(3):
    for col in range(18):
        if (row == 2 and col > 12) or (row == 1 and (13 < col < 17)) or row == 0 and col == 15:
            print(h, end="")
        else:
            print(end=" ")
    print()
# the body
for row in range(10):
    for col in range(18):
        if (row < 10 and col <= 4) or (2 < row < 6 and 4 < col < 13) or (row < 10 and col > 12):
            print(h, end="")
        else:
            print(end=" ")
    print()
# bottom left cone
for row in range(3):
    for col in range(18):
        if (row == 0 and col < 5) or (row == 1 and (0 < col < 4)) or row == 2 and col == 2:
            print(h, end="")
        else:
            print(end=" ")
    print()
