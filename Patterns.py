#patterns

n = int(input())

for i in range(n):
    for j in range(n):
        print("*", end=' ')
    print()

print("\n")

for i in range(n):
    for j in range(i+1):
        print("*", end=' ')
    print()

print("\n")

for i in range(n):
    for j in range(n-i):
        print("*", end=' ')
    print()

print("\n")

for i in range(n):
    for j in range(n-1, i, -1):
        print(" ", end='')
    for k in range(i+1):
        print("* ", end='')
    print()

