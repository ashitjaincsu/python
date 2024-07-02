# Ask the user for the current time and the number of hours to wait for the alarm

current_time = int(input("Enter the current time in hours (0-23): "))
wait_hours = int(input("Enter the number of hours to wait for the alarm: "))

# Validate the input
if current_time < 0 or current_time > 23:
    print("Invalid current time. Please enter a value between 0 and 23.")

elif wait_hours < 0:
    print("Invalid wait hours. Please enter a non-negative value.")

else:
# Calculate the alarm time
    alarm_time = (current_time + wait_hours) % 24

    # Display the result
    print(f"The time when the alarm goes off will be: {alarm_time:02d}:00")
