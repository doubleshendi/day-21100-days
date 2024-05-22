print("Math Game !!")
print()
multiple = int(input("Name your multiples: "))
print()
score = 0
i =0
for i in range(0, multiple):
    print(i,  "x", multiple, "=")
    answer = int(input("Type your answer: "))
    
    if answer == i * multiple:
        print("Great work!")
        score = score+1
        print("Your score is", score )
        print()
    else:
        print("Nope! The answer was", i * multiple)
        print()

print("You scored", score, "out of", multiple)
