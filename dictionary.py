dict={"name":"Fasmil Shan","age":22,"Place":"Kozhikode"}
print(dict)
print(dict["name"])
print(dict["age"])
print(dict["Place"])
print("-----------------------------------")


print(dict.keys())
print(dict.values())
print(dict.items())
print("-----------------------------------")


dict.update({"name":"Fasmil","Place":"Payyoli"})
print(dict)
print("-----------------------------------")



print("The Removed Item :",dict.pop("age"))
print(dict)
print("-----------------------------------")



print("The Removed Item :",dict.popitem())
print(dict)
print("-----------------------------------")


dict.setdefault("city","Kozhikode")
print(dict)
