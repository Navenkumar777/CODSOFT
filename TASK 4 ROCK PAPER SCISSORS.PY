import random

def rock_paper_scissors_unique():
    print("🎮 Welcome to the Ultimate Rock-Paper-Scissors Challenge! 🎮")
    
    # Let the user choose the game length
    while True:
        try:
            rounds = int(input("How many rounds would you like to play? (Best of 3, 5, 10): ").strip())
            if rounds not in [3, 5, 10]:
                raise ValueError
            break
        except ValueError:
            print("Invalid choice! Please choose either 3, 5, or 10 rounds.")
    
    # Initialize scores
    user_score = 0
    computer_score = 0
    round_number = 1

    choices = ["rock", "paper", "scissors"]
    win_messages = {
        "rock": "Rock smashes scissors to dust!",
        "paper": "Paper wraps rock like a gift!",
        "scissors": "Scissors slice paper clean!"
    }

    # Game loop
    while round_number <= rounds:
        print(f"\n🌟 Round {round_number} 🌟")
        user_choice = input("Choose: rock, paper, or scissors? ").strip().lower()

        if user_choice not in choices:
            print("🚫 Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = random.choice(choices)
        print(f"🤖 Computer chose: {computer_choice}")
        
        # Determine winner
        if user_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print(f"🎉 You win this round! {win_messages[user_choice]}")
            user_score += 1
        else:
            print(f"😔 Computer wins this round! {win_messages[computer_choice]}")
            computer_score += 1

        # Update scores
        print(f"🏆 Scores: You: {user_score}, Computer: {computer_score}")
        round_number += 1

    # Final results
    print("\n🔥 Final Results 🔥")
    print(f"Final Scores: You: {user_score}, Computer: {computer_score}")
    if user_score > computer_score:
        print("🎉 Congratulations, you are the Champion!")
    elif user_score < computer_score:
        print("💻 The computer reigns supreme. Better luck next time!")
    else:
        print("🤯 It's a tie overall! Bonus round!")
        # Bonus round
        while True:
            user_choice = input("Bonus Round - Choose rock, paper, or scissors: ").strip().lower()
            computer_choice = random.choice(choices)
            print(f"🤖 Computer chose: {computer_choice}")

            if user_choice not in choices:
                print("🚫 Invalid choice! Please choose again.")
                continue

            if user_choice == computer_choice:
                print("🤝 Bonus round tied! Try again.")
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "paper" and computer_choice == "rock") or \
                 (user_choice == "scissors" and computer_choice == "paper"):
                print(f"🎉 You win the bonus round! {win_messages[user_choice]}")
                print("🏅 You are the Ultimate Champion!")
                break
            else:
                print(f"😔 Computer wins the bonus round! {win_messages[computer_choice]}")
                print("💻 The computer takes the crown this time!")
                break

# Run the unique game
rock_paper_scissors_unique()
