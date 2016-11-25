# Our quiz!
score = 0
name = ""
def quiz():
    global score
    global name

    
    print("Welcome to Pointless Quiz, where it's three out of four to win to win")
    name = input("Enter your name: ")
    print("Hello", name)
    question1()
    question2()
    question3()
    question4()
    
def question1():
    global score
    global name
    print("Which of these isn't a knife")
    print("A. The Kitchen Knife")
    print("B. The Butter Knife")
    print("C. The Cheese Knife")
    print("D. The Spoon")

    answer = input("Answer: ")

    if answer.upper() == "D":
        score = score + 1
        print("Question 1 correct")
        print("Your score is", score, "well done", name)

    else:
        print("Incorrect")
        print("Your score is", score, "bad luck", name)

    
def question2():
    global score
    global name
    print(" ")
    print("What fast food restaurant is most popular in the US")
    print("A. Subway")
    print("B. Wendy's")
    print("C. Mcdonalds")
    print("D. Burger King")

    answer = input("Answer: ")

    if answer.upper() == "C":
        score = score + 1
        print ("Question 2 correct")
        print("Your score is", score, "well done", name)

    

    else:
        print("Incorrect")
        print("Your score is", score, "bad luck", name)

def question3():
    global score
    global name
    print(" ")
    print("Who won the 2004 US presidential election")
    print("A. George W. Bush")
    print("B. John Kerry")
    print("C. Abraham Lincoln")
    print("D. Bill Clinton")

    answer = input("Answer: ")

    if answer.upper() == "A":
        score = score + 1
        print("Question 3 correct")
        print("Your score is", score, "well done", name)
        

    else:
        print("Incorrect")
        print("Your score is", score, "bad luck", name)

def question4():
    global score
    global name
    print(" ")
    print("Which city in the US has the largest population")
    print("A. Swahili")
    print("B. New York")
    print("C. Los Angeles")
    print("D. Phoenix")

    answer = input("Answer: ")

    if answer.upper() == "B":
        score = score + 1
        print("Question 4 correct")
        print("Your score is", score, "well done", name)

    else:
        print("Incorrect")
        print("Your score is", score, "bad luck", name) 

    if score >= 3:
            print(" ")
            print("Winner")
            print(" ")
            print("You have won a holiday for two in Hawaii in the Hapuna Beach Prince Hotel for 2 weeks")

    if score < 3:
            print(" ")
            print("You Lose", name, "Too Bad")

    
    
        
        



# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()

    
    
