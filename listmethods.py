lst=[1,2,3,4,5,6]
# lst[6]=7
lst.append(7)
print(lst)


lst.extend([7,8,9,10])
print(lst)


lst.remove(7)
print(lst)


lst.pop()
print(lst)
print("The Removed Item Is:",lst.pop(7))
print(lst)


lst.insert(3,10)
print(lst)


print("Index Of 7:",lst.index(7))


print(" 7 (count) :",lst.count(7))


lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)


lst.reverse()
print(lst)


lst.clear()
print(lst)
