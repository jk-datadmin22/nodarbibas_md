augstums = 5

for i in range(1, augstums):
    for j in range(i):
        print("*", end=" ")

    print()

for i in range(augstums, 0, -1):
    for j in range(i):
        print("*", end=" ")

    print()

