score = 0
print("Welcome!")
answer1 = input("Capital of France? ")
if answer1.lower() == "paris":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")
print("Score:", score)
