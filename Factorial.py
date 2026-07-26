n = int(input("enter number : "))
i = 1
fact = 1

while i <= n:
    fact *= i
    i += 1

print(f"factorial of {n} :", fact)
