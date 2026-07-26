n = int(input("enter nth term : "))

j = 0
k = 1
print(f"Fibonacci series up to {n} : ", end="")
for i in range(1, n + 1):
    print(j, end=" ")
    l = j + k
    j = k
    k = l
