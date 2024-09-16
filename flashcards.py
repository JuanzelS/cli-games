import json

# Function to load the flashcards data from the JSON file
def load_flashcards(file):
    with open(file, 'r') as f:
        return json.load(f)

# Function to run the flashcard quiz
def run_quiz(data):
    total = len(data["cards"])  # total number of cards
    score = 0  # initialize score to 0

    # Iterate through each flashcard
    for card in data["cards"]:
        guess = input(card["q"] + " > ")  # get user input

        # Check if the user's guess matches the answer (case insensitive)
        if guess.lower() == card["a"].lower():
            score += 1  # increment score for correct answer
            print(f"Correct! Current score: {score}/{total}")
        else:
            print(f"Incorrect! The correct answer was {card['a']}.")
            print(f"Current score: {score}/{total}")

    # Print final message based on score
    print("\nThanks for playing!")
    if score == total:
        print(f"Amazing! You scored {score} out of {total}.")
    elif score > total / 2:
        print(f"Good work! You scored {score} out of {total}.")
    else:
        print(f"You need practice... You scored {score} out of {total}.")

# Main function to execute the flashcard program
if __name__ == "__main__":
    flashcards_data = load_flashcards('me-capitals.json')  # Load the flashcards data
    run_quiz(flashcards_data)  # Start the quiz
