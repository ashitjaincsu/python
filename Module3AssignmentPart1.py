tip_rate = 0.18
tax_rate = 0.07

# Ask the user to enter the charge for the food
food_charge = float(input("Enter the charge for the food: $"))

# Calculate the amounts
tip_amount = food_charge * tip_rate
tax_amount = food_charge * tax_rate
total_amount = food_charge + tip_amount + tax_amount


# Display the results
print(f"\nCharge for the food: ${food_charge:.2f}")
print(f"Tip amount (18%): ${tip_amount:.2f}")
print(f"Sales tax amount (7%): ${tax_amount:.2f}")
print(f"Total amount: ${total_amount:.2f}")
