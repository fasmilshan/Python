age = int(input("Enter your age : "))
if age >= 18:
    drive = input("can you drive ? (yes/no) :")
    if drive.lower() == "yes" :
        print("You are eligible to drive , if you have license")
    else:
        print("you don't have the permit to drive")
else:
    print("you don't have the eligibilty to drive")