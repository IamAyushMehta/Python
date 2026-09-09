def cal_Bill(*items):
    return sum(items)

price = []
n = int(input("enter no of items : "))

for i in range(n):
    price.append(int(input(f"enter price of item no {i+1} : ")))

print(f"total bill : ${cal_Bill(*price)}")
