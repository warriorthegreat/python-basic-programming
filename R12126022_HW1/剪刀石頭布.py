import guess

your_kinds = input("出拳") 
com_kinds = guess.figure_guess()
print(com_kinds)

#贏的情況 
if your_kinds == "scissors" and com_kinds =="paper" :
    print("player win")
elif your_kinds == "rock" and com_kinds =="scissors":
    print("player win")
elif your_kinds == "paper" and com_kinds =="rock":
    print("player win")

#平手
elif your_kinds == "rock" and com_kinds =="rock":
    print("even")
elif your_kinds == "paper" and com_kinds =="paper":
    print("even")
elif your_kinds == "scissors" and com_kinds =="scissors":
    print("even")

else :
    print("com_win!")
