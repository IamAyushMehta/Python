def search(tp, n):
    for i in range(len(tp)):
        if n == tp[i]:
            print("found at index : ", i)
            return
    print("not found")
    
n = int(input("enter number to search : "))
tp = (1,2,3,4,5,6)




search(tp, n)