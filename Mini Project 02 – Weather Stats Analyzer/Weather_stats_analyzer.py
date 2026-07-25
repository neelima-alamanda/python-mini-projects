# Function to find the highest temperature from a list
def find_highest(temperatures):
    return max(temperatures)

# Function to find the lowest temperature from a list
def find_lowest(temperatures):
    return min(temperatures)

# Function to calculate the average temperature from a list
def calculate_average(temperatures):
    return sum(temperatures) / len(temperatures)

# Function to count how many days had temperatures above the average
def count_above_average(temperatures, average):
    count = 0
    for temp in temperatures:
        if temp > average:  # Check if the temperature is above average
            count += 1
    return count  # Return the count of days above average

# Function to convert temperature from Fahrenheit to Celsius
def to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius

# Function to convert temperature from Celsius to Fahrenheit
def to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

# Main function to drive the Weather Stats Analyzer program
def main():
    # Program header
    print("="*50)
    print(f"{'🌤️ WEATHER STATS ANALYZER 🌤️':^50}")
    print("="*50)
    
    # User input: number of days for which temperatures will be recorded
    while True:
        try:
            days = int(input("Enter number of days: "))
            if days > 0:  # Validation: Number of days must be greater than 0
                break
            else:
                print("Number of days must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")  # Error message for invalid input
    
    # Initialize empty lists to store temperatures and day-temperature pairs
    temperatures = []
    daily_temperatures = []

    # Collect temperature input for each day
    for day in range(days):
        while True:
            try:
                temp = float(input(f"Enter Day {day+1} Temperature: "))
                if temp>0:
                    temperatures.append(temp)  # Append the temperature to the list
                    daily_temperatures.append((f"Day {day+1}", temp))  # Create a tuple of day and temperature
                    break
                else:
                    print("Temperature must be in positive")
            except ValueError:
                print("Please enter a valid temperature.")  # Error message for invalid temperature input

    # Output the daily temperatures
    print("\nDaily Temperatures:")
    for day, temp in daily_temperatures:  # Iterate through the list of day-temperature tuples
        print(f"{day:<20} : {temp:.2f}°C")  # Print each day and its corresponding temperature

    # Create a set of unique temperatures (to identify non-repeating temperatures efficiently)
    unique_temperatures = set(temperatures)
    print("Unique Temperatures:", sorted(unique_temperatures))

    # Allow the user to search for a specific temperature in the unique set
    while True:
        try:
            search_temp = float(input("Enter temperature to search: "))
            break
        except ValueError:
            print("Please enter a valid temperature.")  # Error message for invalid input

    # Check if the searched temperature exists in the unique set
    if search_temp in unique_temperatures:
        print(f"{search_temp}°C was recorded.")
    else:
        print(f"{search_temp}°C was not recorded.")

    # Perform temperature analysis
    highest = find_highest(temperatures)  # Get the highest temperature
    lowest = find_lowest(temperatures)  # Get the lowest temperature
    average = calculate_average(temperatures)  # Calculate the average temperature
    count = count_above_average(temperatures, average)  # Count days above average temperature

    # Display the results of the temperature analysis
    print("\nTemperature Analysis")
    print("-" * 35)
    print(f"{'Highest Temperature':<25}: {highest:.2f}°C")
    print(f"{'Lowest Temperature':<25}: {lowest:.2f}°C")
    print(f"{'Average Temperature':<25}: {average:.2f}°C")
    print(f"{'Days Above Average':<25}: {count}")

    # Add a temperature conversion feature
    print("\nTemperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    # Allow the user to choose a conversion option and validate the choice
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in (1, 2):  # Ensure the input is 1 or 2
                break
            else:
                print("Choose either 1 or 2.")  # Invalid choice error handling
        except ValueError:
            print("Invalid choice.")  # Error message for invalid input

    # Perform the selected temperature conversion
    if choice == 1:
        while True:
            try:
                celsius = float(input("Enter Celsius: "))
                print(f"Fahrenheit: {to_fahrenheit(celsius):.2f}°F")
                break
            except ValueError:
                print("Enter a valid temperature.")  # Error message for invalid input
    elif choice == 2:
        while True:
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                print(f"Celsius: {to_celsius(fahrenheit):.2f}°C")
                break
            except ValueError:
                print("Enter a valid Temperature")  # Error message for invalid input
    
    # Closing message
    print("\n" + "=" * 50)
    print("Thank you for using Weather Stats Analyzer!")
    print("=" * 50)

# Entry point of the program
if __name__ == "__main__":
    main()