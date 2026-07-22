a = int(input("enter a : "))
op = input("enter operator : ")
b = int(input("enter b : "))

match op:
    case "+":
        print("res : ", a + b)

    case "-":
        print("res : ", a - b)

    case "*":
        print("res : ", a * b)

    case "/":
        if b != 0:
            print("res : ", a / b)
        else:
            print("res : cant divided by zero")

    case "**":
        print("res : ", a**b)
