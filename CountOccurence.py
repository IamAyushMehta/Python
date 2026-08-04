l = [1, 2, 3, 1, 1, 2, 5, 5]
element = int(input("Enter the element to count: "))

# print(f"{element} appear at : ", l.count(element), "times")

count = 0
for i in range(0, len(l)):
    if l[i] == element:
        count += 1


print("List:", l)
print(f"{element} appears {count} time(s).")
