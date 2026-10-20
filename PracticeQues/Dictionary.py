import numpy as np
# student = {
#     "name" : "ayush",
#     "age" : 21,
#     "course" : "BCA",
#     "city" : "Patna"
# }

# # keys = ["name", "age", "course", "city"]
# # values = ["ayush", 21, "BCA", "Patna"]
# # res = dict(zip(keys, values))
# # print(res)

# # d1 = {
# #     "name" : "Rahul",
# #     "age" : 21,
# #     "course" : "BCA"
# # }

# # d2 = {
# #     "course" : "BCA",
# #     "city" : "Delhi"
# # }

# # d1.update(d2)
# # print(d1)

# marks = {
#     "python" : 80,
#     "java" : 75,
#     "dbms" : 85,
#     "math" : 70
# }

# # print(sum(marks.values())/len(marks))
# highest_marks = 0
# highest_subject = ""
# for key, value in marks.items():
#     if highest_marks < value:
#         highest_marks = value
#         highest_subject = key

# print(highest_subject,":",highest_marks)

# lowest_marks = 100
# subject = ""
# for i,j in marks.items():
#     if lowest_marks > j:
#         lowest_marks = j
#         subject = i
# print(lowest_marks, subject)

# subject = max(marks, key=marks.get)
# print(subject)

# s1 = "ayushmehta"
# lst = []

# for i in s1:
#     if i not in lst:
#         lst.append(i)

# for i in lst:
#     count = 0
#     for j in s1:
#         if i == j:
#             count += 1
#     print(f"{i} : {count}")


# str = "ayushmehta"
# freq = {}
# for i in str:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
# print(freq)

# sentence = "hello my name is"
# lst = list(sentence.split())
# word = 0
# for i in lst:
#     word += 1
# print(word)

# marks = {"Python": 85, "Java": 72, "DBMS": 90, "Math": 78, "Networking": 82}

# for i, j in marks.items():
#     if j >= 80:
#         print(f"{i} : {j}")

student = {"name": "Rahul", "marks": {"Python": 85, "DBMS": 90, "Math": 78}}
print(f"mean : {np.mean(list(student['marks'].values()))}")