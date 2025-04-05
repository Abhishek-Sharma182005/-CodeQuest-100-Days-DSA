turn=input("Which path do you choose? (left/right): ")
#taking input of user's decision 
if turn == "left" or turn == "Left" or turn == "LEFT" :
    print("You found a hidden tunnel! You're safe. 🚀")
#if user took left
elif turn == "right" or turn == "Right" or turn == "RIGHT" :
    print("Oh no! The Glitch's trap was here! Try again.😨")
#if user took right
else:
    print("Choose left/right")
#if user write something else