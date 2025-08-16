while True:
 num1 = input("give me a number: (or use q to quit)")
 if num1.lower() == "q":
  break
 num1 = float(num1)
 num2 = float(input("give me another number: "))
 print("Choose an operation:")
 print("m = multiply")
 print("d = divide")
 print("a = add")
 print("s = subtract")
 operator = input("Your choice: ").lower()
 if operator == "m":
  print(num1*num2)
 elif operator == "d":
  try:
   print(num1/num2)
  except ZeroDivisionError:
   print("division not possible")
 elif operator == "a":
  print(num1+num2)
 elif operator == "s":
  print (num1-num2)
 else:
  print("invalid operator!")