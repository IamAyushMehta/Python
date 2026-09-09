# Q1
# student = {
#     "ayush" : [10,11,12],
#     "rohit" : [10,11,15],
#     "ranjan" : [10,14,12],
#     "gyan" : [10,18,12],
#     "aryan" : [14,11,12],
# }

# highest_name = ""
# highest_marks = 0

# for names, marks in student.items():
#     total = sum(marks)
#     average = total/len(marks)
#     print(names, " total marks : ", total)
#     print(names, " average marks : ", average)

#     if highest_marks < total:
#         highest_marks = total
#         highest_name = names

# print(highest_name, "scored highest marks :", highest_marks)

# Q2
# n = int(input("enter the range : "))
# lst = []
# for i in range(n):
#     lst.append(int(input("enter the numbers : ")))

# print(sorted(list(set(lst))))

# Q3
# bca = {1,2,3,4,5}
# bba = {1,3,5}
# all_student = {1,2,3,4,5,6,7,8,9,10}

# both_courses = bca & bba
# first_course = bca - bba
# either_course = bca | bba
# neither_course = all_student - either_course

# print(both_courses)
# print(first_course)
# print(either_course)
# print(neither_course)

# Q4
# employee = {
#     "101" : ("ayush", "bca", 55000),
#     "102" : ("aryan", "bba", 35000),
#     "103" : ("ranjan", "bca", 10000),
#     "104" : ("rohit", "bba", 90000),
#     "105" : ("gyan", "ba", 75000),
#     "106" : ("akash", "ba", 60000),
#     "107" : ("jhon", "bca", 25000),
# }

# for employeeID, i in employee.items():
#     if i[2] >= 40000:
#         print(i)

# Q5
sentence = input("enter sentence : ")
words = sentence.lower().split()

lst = []
count = []
res = []
for i in words:
    lst.append(i)

lst = sorted(list(set(lst)))

for i in lst:
    count.append(words.count(i))

for i in range(len(lst)):
    # res.append(lst[i])
    # res.append(count[i])
    print(lst[i], "=", count[i])

# print(res)
