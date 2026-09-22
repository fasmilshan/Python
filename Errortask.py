class Greatorthan100Error(Exception):
    pass
class Lessthan0Error(Exception):
    pass
try:
 mark=int(input("Enter Your Mark :"))
except ValueError:
    print("----!----Mark Must be A NUMber----!----")
else:    
 if mark > 100:
    raise Greatorthan100Error("Cant Get Above 100")
 elif mark < 0:
    raise Lessthan0Error("Its Below Zero !")
 else:
    print(f"Your Scored '{mark}'")
print("Thank Youuuu \n--------------------------------")

