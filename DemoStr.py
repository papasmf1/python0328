# DemoStr.py

#print(dir(str))

strA = "<<<  spam and ham  >>>"
print(strA)
print(strA.strip("<> "))

result = strA.strip("<> ")
print(result)

strB = "python is very powerful"
print(len(strB))
print(strB.capitalize())
print(strB.count("p",7))
print(strB.endswith("ful"))

result2 = result.replace("spam", "spam egg")
print(result2)

lst = result2.split()
print(lst)
print("다시 합치기:", ":)".join(lst))



