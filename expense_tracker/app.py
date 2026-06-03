import os  # <--- 1. ADD THIS AT THE VERY TOP

while True:
    print("\n--- EXPENSE TRACKER MENU ---")
    print("1. Add New Expense")
    print("2. View Total Expenses")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        category = input("Enter category (e.g., Food, Transport): ")
        amount = input("Enter amount: ")
        date = input("Enter date (YYYY-MM-DD): ")
        
        with open("expenses.txt", "a") as file:
            file.write(f"{category},{amount},{date}\n")
            
        print("\nExpense saved successfully!")
        
    elif choice == "2":
        print("\n--- YOUR EXPENSES ---")
        total = 0.0
        
        # 2. USE IF/ELSE TO CHECK IF THE FILE EXISTS
        if os.path.exists("expenses.txt"):
            with open("expenses.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        category = parts[0]
                        amount = float(parts[1])
                        date = parts[2]
                        print(f"- {date} | {category}: ${amount:.2f}")
                        total += amount
            print("-" * 25)
            print(f"TOTAL SPENT: ${total:.2f}")
            
        else: # 3. IF THE FILE DOES NOT EXIST, DO THIS
            print("No expenses recorded yet! Try adding one first.")
        
    elif choice == "3":
        print("\nGoodbye!")
        break
        
    else:
        print("\nInvalid choice! Please type 1, 2, or 3.")