tasks = []
def add_text(text):
    tasks.append(text)
def remove_text(text):
    if text in tasks:
        tasks.remove(text)
    else:
        print("The text not found!")
def view_text():
    for key, value in enumerate(tasks):
        print(f"{key + 1}: {value}")
import os
def running_function():
    while True:
        print("Task planner menu: ")
        print("1. Add text")
        print("2. Delete text")
        print("3. View text")
        print("4. Quit")

        choice = input("Enter the choice (1-4)")
        if choice == "1":
            text = input("Enter the text: ")
            add_text(text)
        elif choice == "2":
            text = input("Delete the text: ")
            remove_text(text)
        elif choice == "3":
            view_text()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            os.abort()
print(running_function())