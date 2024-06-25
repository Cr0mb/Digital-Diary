import os
import getpass
from datetime import datetime

# Function to clear screen for better UI interaction
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to save diary entry to file
def save_entry(entry, filename):
    with open(filename, 'a') as file:
        file.write(entry + '\n')

# Function to read all diary entries from file
def read_entries(filename):
    entries = []
    with open(filename, 'r') as file:
        entries = file.readlines()
    return entries

# Function to display diary entries
def display_entries(entries):
    for i, entry in enumerate(entries, 1):
        print(f"Entry {i}:")
        print(entry)

# Main function to manage diary application
def main():
    clear_screen()
    print("Welcome to Your Digital Diary!\n")
    
    # Get current user's username for diary file
    username = getpass.getuser()
    filename = f"{username}_diary.txt"
    
    # Create diary file if it doesn't exist
    if not os.path.exists(filename):
        with open(filename, 'w'):  # Create file
            pass

    while True:
        print("\nWhat would you like to do?")
        print("1. Write a new diary entry")
        print("2. View all diary entries")
        print("3. Exit\n")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            clear_screen()
            print("Write your entry (press Enter twice to save):")
            entry_lines = []
            while True:
                line = input()
                if line:
                    entry_lines.append(line)
                else:
                    break
            entry = "\n".join(entry_lines)
            
            # Add timestamp to the entry
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = f"{timestamp}\n{entry}\n"
            
            # Save the entry to file
            save_entry(entry, filename)
            clear_screen()
            print("Entry saved successfully!\n")
        
        elif choice == '2':
            clear_screen()
            print("Here are all your diary entries:\n")
            entries = read_entries(filename)
            if entries:
                display_entries(entries)
            else:
                print("No entries found.\n")
        
        elif choice == '3':
            clear_screen()
            print("Thank you for using Your Digital Diary. Goodbye!")
            break
        
        else:
            clear_screen()
            print("Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
