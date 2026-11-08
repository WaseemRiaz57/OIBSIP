while True:
    print("\n===== BMI CALCULATOR =====")

    # Step 2: Get weight
    while True:
        try:
            weight = float(input("Enter your weight (kg): "))

            if weight <= 0:
                print("Error: Weight must be greater than zero.")
            else:
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Step 3: Get height
    while True:
        try:
            height = float(input("Enter your height (meters): "))

            if height <= 0:
                print("Error: Height must be greater than zero.")
            else:
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Step 5: Calculate BMI
    bmi = weight / (height ** 2)

    print(f"\nYour BMI is: {bmi:.2f}")

    # Step 6: Determine category
    if bmi < 18.5:
        category = "Underweight"
        message = "Your weight is below the normal range."

    elif bmi < 25:
        category = "Normal"
        message = "Your weight is within the normal range."

    elif bmi < 30:
        category = "Overweight"
        message = "Your weight is above the normal range."

    else:
        category = "Obese"
        message = "Your BMI is in the obese range."

    # Step 7: Display result
    print("Category:", category)
    print(message)

    # Step 8: Ask to calculate again
    choice = input("\nDo you want to calculate again? (yes/no): ").lower()

    if choice != "yes":
        print("Thank you for using BMI Calculator!")
        break
