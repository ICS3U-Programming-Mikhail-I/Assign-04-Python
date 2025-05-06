# Author: 2025 Mikhail Ibrahim
# Date: May 5th, 2025
# Description: A crash-proof Python program simulating a virtual wallet.
# The user can earn or spend money, view balance, and try to reach $1000.
# The program prevents crashes due to invalid input and exits safely.


def main():
    print("Welcome to the Spend & Earn Money Simulator!")
    print("Manage your virtual wallet by earning or spending.")
    print("Reach your $1000 goal, or avoid going broke!\n")

    # Initialize wallet and variables
    balance = 100
    goal = 1000
    transaction_count = 0

    # Main game loop
    while True:
        print("\n--- Menu ---")
        print("1. Work as a Cashier ($50)")
        print("2. Work as a Freelancer ($150)")
        print("3. Work as a Programmer ($300)")
        print("4. Buy Money (Add with 10% bonus)")
        print("5. Invest Money (5% return)")
        print("6. Check Balance")
        print("7. Quit")

        try:
            choice = int(input("Choose an option (1-7): "))

            if choice == 1:
                balance += 50
                transaction_count += 1
                print("You worked as a Cashier and earned $50.")
                print("New balance: $", balance)

            if choice == 2:
                balance += 150
                transaction_count += 1
                print("You worked as a Freelancer and earned $150.")
                print("New balance: $", balance)

            if choice == 3:
                balance += 300
                transaction_count += 1
                print("You worked as a Programmer and earned $300.")
                print("New balance: $", balance)

            if choice == 4:
                try:
                    amount = float(input("How much money do you want to buy? $"))
                    if amount <= 0:
                        print("Amount must be positive.")
                    else:
                        if balance >= amount:
                            bonus = amount * 0.10
                            balance -= amount
                            balance += amount + bonus
                            transaction_count += 1
                            print(
                                "Purchased virtual money. Bonus added: $",
                                round(bonus, 2),
                            )
                            print("New balance: $", round(balance, 2))
                        else:
                            print("Insufficient funds to buy money.")
                except ValueError:
                    print("Invalid amount entered.")

            if choice == 5:
                try:
                    amount = float(input("How much do you want to invest? $"))
                    if amount <= 0:
                        print("Investment must be positive.")
                    else:
                        if balance >= amount:
                            balance -= amount
                            gain = amount * 0.05
                            balance += amount + gain
                            transaction_count += 1
                            print(
                                "You invested $",
                                round(amount, 2),
                                " and earned $",
                                round(gain, 2),
                            )
                            print("New balance: $", round(balance, 2))
                        else:
                            print("Insufficient funds to invest.")
                except ValueError:
                    print("Invalid amount entered.")

            if choice == 6:
                print("Your current balance is: $", round(balance, 2))
                print("Transactions completed:", transaction_count)

            if choice == 7:
                print("\nThank you for playing!")
                print("Final balance: $", round(balance, 2))
                print("Total transactions:", transaction_count)
                break

            if choice < 1 or choice > 7:
                print("Invalid option. Please choose a number between 1 and 7.")

            # Check end-game conditions after each action
            if balance <= 0:
                print("\nYou are bankrupt! Game over.")
                break
            if balance >= goal:
                print(
                    "\n🎉 Congratulations! You've reached your savings goal of $1000!"
                )
                break

        except ValueError:
            print("Invalid input. Please enter a number from 1 to 7.")


# Run the game
if __name__ == "__main__":
    main()
