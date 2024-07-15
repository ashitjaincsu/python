def main():
    # Ask the user for the number of years
    years = int(input("Enter the number of years: "))

    # Initialize variables to hold the total number of months and the total rainfall
    months = 0
    rain = 0.0

    # Outer loop to iterate over each year
    for year in range(1, years + 1):
        print(f"\nYear {year}")

        for month in range(1, 13):
            rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
            if rainfall < 0:
                print("Rainfall cannot be negative. Please enter a valid number.")
            rain += rainfall
            months += 1

    # Calculate the average rainfall per month
    average_rainfall = rain / months

    # Display the results
    print(f"\nNumber of months: {months}")
    print(f"Total inches of rainfall: {rain:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f}")


# Run the main function
if __name__ == "__main__":
    main()