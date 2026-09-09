EmployeeRecords = {
    100 : ["ayush", "bca", 40000],
    101 : ["aryan", "bba", 35000],
    102 : ["rohit", "bca", 210000],
}

for i, j in EmployeeRecords.items():
    if  j[2] >= 40000:
        print(EmployeeRecords[i])