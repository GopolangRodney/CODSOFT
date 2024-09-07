num_one = int(input ("Enter 1st Number (999 to exit)"))

while num_one != 999:
    if num_one == 999:
        break
    elif num_one != 999:
            operator = input ("Enter Operator")
            num_two = int(input ("Enter 2nd Number"))

    if operator == "-":
          result = num_one - num_two

    elif operator == "+":
            result = num_one + num_two

    elif operator == "*":
             result = num_one * num_two

    elif operator == "/":
            if num_two != 0:
              result = num_one / num_two
            else:
                print ("Error: Division by zero is not allowed.")

    else:
            print ("Error: Invalid operator. Please use +, -, *, or /.")

    print ("Result: ", result)

    num_one = int(input ("Enter 1st Number (999 to exit)"))