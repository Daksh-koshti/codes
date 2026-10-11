print("Welcome to the mathtable program\n")
while True:
    while True:
       print("please  enter a number to generate its multiplication table:")
       input_number = int(input())
       if input_number<1 or input_number>99:
        print("please enter a number between 1 to 99")
       else:
        break

    for i in range (1, 11):
     print(input_number, "X", i, "=", input_number * i)

    print("\n Do you want to generate another multiplication table? (yes/no)")
    choice = input().strip().lower()
    if choice != "yes":
      print("Thank you for using the mathtable program")   
      break
    print ("\n" + "="*40 + "\nStarting a new table...\n" + "="*40 + "\n")

#while True:
#    # Inner loop to get a valid number
#    while True:
#        print("Please enter a number to generate its multiplication table:")
#        input_number = int(input())
#        if input_number < 1 or input_number > 99:
#            print("Please enter a number between 1 to 99")
#        else:
#            break
#
#    # Generate and print the table
#    for i in range(1, 11):
#        print(input_number, "X", i, "=", input_number * i)
#        
#    # Ask if the user wants to repeat
#    print("\nDo you want to generate another multiplication table? (yes/no)")
#    if input().lower() != "yes":
#        print("Thank you for using the mathtable program")
#        break  # Exits the outer loop and ends the program