task = input("What task do you want to be reminded of? ").title()
task_priority = input(
    "What is the priority of this task (high, medium, low)? ").lower().strip()
time_bound = input(
    "Is this task time-bound? (yes/no) ").lower().strip() == "yes"
match task_priority:
    case "high":
        if time_bound:
            print("'" + task + "'",
                  " is a high priority task that requires immediate attention today!")
        elif not time_bound:
            print("'" + task + "'",
                  " is a high priority task. Consider completing it when you have free time.")

    case "medium":
        if time_bound:
            print("'" + task + "'",
                  " is a medium priority task that requires immediate attention today!")
        elif not time_bound:
            print("'" + task + "'",
                  " is a medium priority task. Consider completing it when you have free time.")

    case "low":
        if time_bound:
            print("'" + task + "'",
                  " is a low priority task that requires immediate attention today")
        elif not time_bound:
            print("'" + task + "'",
                  " is a low priority task. Consider completing it when you have free time.")

    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
