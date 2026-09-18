try:
    num1=int(input("Enter First Number :"))
    num2=int(input("Enter Second Number :"))
    result=num1 / num2
      
except ValueError:
    print("You have an Error! it Must be a Number!")

except ZeroDivisionError:
    print("You are Dividing By 0")
    
else:
    print(f"The Result Of Your Operation : {result} ")
    
finally:
    print("--------------------------------------------------")


