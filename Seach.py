def search(tp, n):
    for i in range(len(tp)):
        if n == tp[i]:
            print("found at index : ", i)
            return
    print("not found")
    
tp = (1,2,3,4,5,6)

n = int(input("enter number to search : "))

search(tp, n)