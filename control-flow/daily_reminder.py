Task = input("What task do you want to be reminded of? ").title()
Priority = input(
    "What is the priority of this task (high, medium, low)? ").lower().strip()
Time_Bound = input(
    "Is this task time-bound? (yes/no) ").lower().strip() == "yes"
match Priority:
    case "high":
        if Time_Bound:
            print("'" + Task + "'",
                  " is a high priority task that requires immediate attention today!")
        elif not Time_Bound:
            print("'" + Task + "'",
                  " is a high priority task. Consider completing it when you have free time.")

    case "medium":
        if Time_Bound:
            print("'" + Task + "'",
                  " is a medium priority task that requires immediate attention today!")
        elif not Time_Bound:
            print("'" + Task + "'",
                  " is a medium priority task. Consider completing it when you have free time.")

    case "low":
        if Time_Bound:
            print("'" + Task + "'",
                  " is a low priority task that requires immediate attention today")
        elif not Time_Bound:
            print("'" + Task + "'",
                  " is a low priority task. Consider completing it when you have free time.")

    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
