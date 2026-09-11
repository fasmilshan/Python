while True:
 print("Calculator")
 print("-----------")
 print("1.Addition")
 print("2.Substarction")
 print("3.Division")
 print("4.Multiplication")
 print("5.Exit")
 choice=input("Enter Your Choice : 1/2/3/4/5 =:")
 if choice == "1":
    n1=float(input("Enetr Your First Number: "))
    n2=float(input("Enter Your Second Number: "))
    print(n1,"+",n2,"=",n1+n2)
 elif choice== "2":
    n1=float(input("Enetr Your First Number: "))
    n2=float(input("Enter Your Second Number: "))
    print(n1,"-",n2,"=",n1-n2)
 elif choice== "3":
    n1=float(input("Enetr Your First Number: "))
    n2=float(input("Enter Your Second Number: "))
    print(n1,"%",n2,"=",n1/n2)
 elif choice== "4":
    n1=float(input("Enetr Your First Number: "))
    n2=float(input("Enter Your Second Number: "))
    print(n1,"x",n2,"=",n1*n2)
 elif choice== "5":
    break
 elif choice == " ":
    print("Please Choose Your Choice From(1,2,3,4,5)!")
 else: 
      print("Invalid Option")