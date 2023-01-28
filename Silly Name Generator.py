import sys, random

print("Welcome to the Silly Name Generator\n")
print("Create a silly name:\n\n")
first = ('Baby', 'Bad News', 'Burpy', 'Bill', 'Beenie', 'Bpb Stinkbug', 'Bowel', 'Boxelder', "Bud 'Lite'", 'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield', 'Chewy', 'Chigger', 'Worms')
last = ('Apple', 'Bigmeat', 'Bloominshine', 'Booger-eater', 'Breeds', 'Clovenhoof', 'Clutterbuck')

#main while loop terminates when user enters n
while True:
    firstName = random.choice(first)
    lastName = random.choice(last)

    print("\n")
    print("{} {}".format(firstName, lastName), file=sys.stderr)
    print("\n")

    try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
    if try_again.lower() == "n":
        break

input("\nPress Enter to exit.")
                
