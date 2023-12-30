import json
import random
import time
import os

# Constants
LEADERBOARD_FILE = "leaderboard.json"
WORDS_FILE = "word_categories.json"
WORD_CATEGORY = "word_categories.json"

def load_leaderboard():
    with open(LEADERBOARD_FILE) as file:
        leaderboard = json.load(file)
    print(leaderboard)
    return leaderboard

def update_leaderboard(username, wpm):
    leaderboard = load_leaderboard()
    leaderboard.append({"username": username, "wpm": wpm})
    leaderboard.sort(key=lambda x: x["wpm"], reverse=True)
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file)

def show_leaderboard():
    leaderboard = load_leaderboard()
    print("\nLeaderboard:")
    for idx, entry in enumerate(leaderboard, start=1):
        print(f"{idx}. {entry['username']} - {entry['wpm']} WPM")

def load_cat():
    with open(WORD_CATEGORY) as file:
        categories = json.load(file)
    res = {}
    for idx, entry in enumerate(categories, start=1):
        res[idx] = entry
    return res

def load_words_from_json(category):
    with open(WORDS_FILE) as file:
        words_data = json.load(file)
    return words_data[category]

def get_user_input():
    return input("Type the words above: ")

def main():
    print("Welcome to the Terminal Typing Master!")

    username = input("Enter your username: ")

    while True:
        print("\nOptions:")
        print("1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            categories = load_cat()
            print(categories)
            for idx in range(1,11):
                print(f"{idx}. {categories[idx]}")

            choice = input('Select the Category:')
            words = load_words_from_json(categories[int(choice)])
            random.shuffle(words)
            choice = input('Enter number of words 0-200 :')
            words_to_type = words[:int(choice)]
            print(f"\nType the following words:\n")

            time_taken = 0
            for each in words_to_type:
                print(each)

                start_time = time.time()
                user_input = get_user_input()
                end_time = time.time()
                if(user_input == each):
                    print(f"\033[32m{user_input}\033[0m")
                else:
                    print(f"\033[31m{user_input}\033[0m")
                time_taken += end_time - start_time

            wpm = int((int(choice) / time_taken) * 60)

            print(f"\nWords Typed: {choice}")
            print(f"Time Taken: {time_taken:.2f} seconds")
            print(f"Words Per Minute: {wpm} WPM")

            update_leaderboard(username, wpm)

        elif choice == "2":
            show_leaderboard()

        elif choice == "3":
            print("Exiting Terminal Typing Master. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
