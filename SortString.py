s1 = input("enter string : ")
s2 = input("enter string : ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not an anagram")
