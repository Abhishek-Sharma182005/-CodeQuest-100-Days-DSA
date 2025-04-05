# Make a Decision

way=input("Which path do you choose? (left/right):\n")

if way=="left":
    print("You found a hidden tunnel! You're safe.")
elif way=="right":
    print("Oh no! The Glitch's trap was here! Try again.")
else:
    print("Invalid choice. Please enter 'left' or 'right'.")