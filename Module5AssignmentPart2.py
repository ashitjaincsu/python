def calculate_points(books):
    # Determine points based on the number of books purchased
    if books < 2:
        return 0
    elif books < 4:
        return 5
    elif books < 6:
        return 15
    elif books < 8:
        return 30
    else:
        return 60

def main():

    books_purchased = int(input("Enter the number of books purchased this month: "))
    if books_purchased < 0:
        print("The number of books cannot be negative. Please enter a valid number.")

    points_awarded = calculate_points(books_purchased)

    print(f"Points awarded: {points_awarded}")

# Run the main function
if __name__ == "__main__":
    main()