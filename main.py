temp = input("Enter temperature: ")
unit = input("Enter unit in F/f or C/c: ")
if unit == "F" or unit == "f":
  temp = float(temp)
  print(str(temp)) + "° in Fahrenheit is equivalent to " + str((temp-32)*5/9 + "° Celsius.")
elif unit == "C" or unit == "c":
  temp = float(temp)
  print(str(temp) + "° in Celsius is equivalent to " + str(temp*9/5+32) + "° Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")  
