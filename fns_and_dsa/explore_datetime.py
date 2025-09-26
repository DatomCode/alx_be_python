from datetime import datetime, timedelta


def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format it as YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date


def calculate_future_date(current_date, days_to_add):
    # Add the given number of days
    future_date = current_date + timedelta(days=days_to_add)
    # Print only the date in YYYY-MM-DD format
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date


def main():
    # Part 1: Show current date and time
    current_date = display_current_datetime()

    # Part 2: Ask user for days to add
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("❌ Please enter a valid integer for the number of days.")


if __name__ == "__main__":
    main()
