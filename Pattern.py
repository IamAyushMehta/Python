n = 5
# for i in range(i, n + 1):
#     j = 1
#     for j in range(j, i + 1):
#         print("*", end="")
#     print()

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
