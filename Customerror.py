class DrivingError(Exception):
    pass

age=int(input("Enter Your Age :"))
if age >=18 :
    print("You Are Ready to Drive ")
else:
    # raise Exception("Dont You has to be 18 or above!")
    # raise ValueError("The Age Must be 18 or Above!")
    raise DrivingError("You Cant Drive!")
