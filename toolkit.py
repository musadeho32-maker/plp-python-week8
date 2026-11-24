import random


# Tool 1: A calculator that performs four basic operations.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))

        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Enter your choice: ")

        if operation == "1":
            result = first + second
        elif operation == "2":
            result = first - second
        elif operation == "3":
            result = first * second
        elif operation == "4":
            if second == 0:
                print("You cannot divide by zero.")
                return
            result = first / second
        else:
            print("Invalid operation. Please try again.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: A to-do list where users can add, view and remove tasks.
def todo_list(tasks):
    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            task = input("Enter your task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if not tasks:
                print("Your task list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    number = int(input("Enter the task number to remove: "))

                    if 1 <= number <= len(tasks):
                        removed = tasks.pop(number - 1)
                        print(f"Removed: {removed}")
                    else:
                        print("That task number does not exist.")

                except ValueError:
                    print("Please enter a valid whole number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")


# Tool 3: A number guessing game with repeated attempts.
def guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n--- Number Guessing Game ---")
    print("I am thinking of a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 10:
                print("Please choose a number between 1 and 10.")
            else:
                attempts += 1

                if guess < secret_number:
                    print("Too low! Try again.")
                elif guess > secret_number:
                    print("Too high! Try again.")
                else:
                    print(
                        f"Congratulations! You guessed correctly "
                        f"in {attempts} attempts."
                    )
                    break

        except ValueError:
            print("Please enter a valid whole number.")


# Main menu: keeps the toolkit running until the user chooses Quit.
def main():
    tasks = []

    print("===================================")
    print(" Welcome to Musa's Personal Toolkit")
    print("===================================")

    while True:
        print("\nChoose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            todo_list(tasks)
        elif choice == "3":
            guessing_game()
        elif choice == "4":
            print("Thank you for using my toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 4.")


if __name__ == "__main__":
    main()
