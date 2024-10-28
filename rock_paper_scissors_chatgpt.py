import random

def get_user_choice():
    while True:
        user = input("What's your choice? 'r' for Rock, 'p' for Paper, and 's' for Scissors (or 'q' to quit)\n").lower()
        if user in ['r', 'p', 's', 'q']:
            return user
        else:
            print("Invalid choice. Please try again.")

def determine_winner(user, pc):
    if user == pc:
        return "It's a tie!"
    elif (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or (user == 's' and pc == 'p'):
        return "You won!"
    else:
        return "You lose!"

def main():
    user_score = 0
    pc_score = 0

    while True:
        user = get_user_choice()
        if user == 'q':
            break
        
        pc = random.choice(['r', 'p', 's'])
        
        print(f"User played: {user}")
        print(f"PC played: {pc}")

        result = determine_winner(user, pc)
        print(result)

        if "won" in result:
            user_score += 1
        elif "lose" in result:
            pc_score += 1

        print(f"Score - You: {user_score} | PC: {pc_score}\n")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()