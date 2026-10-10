for i in range(1,6):
    print("* "*i)


for i in range(1,6):
    print(" " * (6 - i) + "*" * i)
#n = 5   ---same code
#for i in range(1, n + 1):
#  print(" " * (n - i) + "*" * i)


#pyramind
for i in range(1,6):
    print(" " * (6 - i) + "*" * (2 * i - 1))

#plus pattern
n = 5

for i in range(n):
    for j in range(n):
        if i == n // 2 or j == n // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#hollow square
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#hollow Diamond
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")

    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end="")

    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print("*", end="")
        else:
            print(" ", end="")
    print()