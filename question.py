while True:
    score = 0
    wrong_answers = ""

    print("Welcome to the MCQ Quiz App!\n")

    # Question 1
    print("1. What is the capital of France?")
    print("a) Berlin")
    print("b) Madrid")
    print("c) Paris")
    print("d) Rome")
    a1 = input("Your answer (a/b/c/d): ")
    if a1.lower() == "c":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is c) Paris\n")
        wrong_answers += "1. The capital of France is Paris. You answered: " + a1 + "\n"

    # Question 2
    print("2. Which planet is known as the Red Planet?")
    print("a) Earth")
    print("b) Mars")
    print("c) Jupiter")
    print("d) Venus")
    a2 = input("Your answer (a/b/c/d): ")
    if a2.lower() == "b":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is b) Mars\n")
        wrong_answers += "2. The Red Planet is Mars. You answered: " + a2 + "\n"

    # Question 3
    print("3. Who wrote 'Romeo and Juliet'?")
    print("a) Charles Dickens")
    print("b) Mark Twain")
    print("c) William Shakespeare")
    print("d) Jane Austen")
    a3 = input("Your answer (a/b/c/d): ")
    if a3.lower() == "c":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is c) William Shakespeare\n")
        wrong_answers += "3. Romeo and Juliet was written by William Shakespeare. You answered: " + a3 + "\n"

    # Question 4
    print("4. What is the largest ocean on Earth?")
    print("a) Atlantic Ocean")
    print("b) Indian Ocean")
    print("c) Arctic Ocean")
    print("d) Pacific Ocean")
    a4 = input("Your answer (a/b/c/d): ")
    if a4.lower() == "d":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is d) Pacific Ocean\n")
        wrong_answers += "4. The largest ocean is Pacific Ocean. You answered: " + a4 + "\n"

    # Question 5
    print("5. What is the boiling point of water at sea level (°C)?")
    print("a) 90")
    print("b) 80")
    print("c) 100")
    print("d) 120")
    a5 = input("Your answer (a/b/c/d): ")
    if a5.lower() == "c":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is c) 100\n")
        wrong_answers += "5. Water boils at 100°C at sea level. You answered: " + a5 + "\n"

    # Question 6
    print("6. Who painted the Mona Lisa?")
    print("a) Leonardo da Vinci")
    print("b) Pablo Picasso")
    print("c) Vincent van Gogh")
    print("d) Claude Monet")
    a6 = input("Your answer (a/b/c/d): ")
    if a6.lower() == "a":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is a) Leonardo da Vinci\n")
        wrong_answers += "6. Mona Lisa was painted by Leonardo da Vinci. You answered: " + a6 + "\n"

    # Question 7
    print("7. What is the largest mammal in the world?")
    print("a) Elephant")
    print("b) Blue Whale")
    print("c) Giraffe")
    print("d) Hippopotamus")
    a7 = input("Your answer (a/b/c/d): ")
    if a7.lower() == "b":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is b) Blue Whale\n")
        wrong_answers += "7. The largest mammal is Blue Whale. You answered: " + a7 + "\n"

    # Question 8
    print("8. What gas do plants absorb from the atmosphere?")
    print("a) Oxygen")
    print("b) Nitrogen")
    print("c) Carbon Dioxide")
    print("d) Hydrogen")
    a8 = input("Your answer (a/b/c/d): ")
    if a8.lower() == "c":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is c) Carbon Dioxide\n")
        wrong_answers += "8. Plants absorb carbon dioxide. You answered: " + a8 + "\n"

    # Question 9
    print("9. Who is known as the father of computers?")
    print("a) Charles Babbage")
    print("b) Alan Turing")
    print("c) Bill Gates")
    print("d) Steve Jobs")
    a9 = input("Your answer (a/b/c/d): ")
    if a9.lower() == "a":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is a) Charles Babbage\n")
        wrong_answers += "9. Charles Babbage is the father of computers. You answered: " + a9 + "\n"

    # Question 10
    print("10. What is H2O commonly known as?")
    print("a) Hydrochloric Acid")
    print("b) Water")
    print("c) Oxygen")
    print("d) Ammonia")
    a10 = input("Your answer (a/b/c/d): ")
    if a10.lower() == "b":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is b) Water\n")
        wrong_answers += "10. H2O is water. You answered: " + a10 + "\n"

    # Question 11
    print("11. Which country gifted the Statue of Liberty to the USA?")
    print("a) England")
    print("b) France")
    print("c) Germany")
    print("d) Spain")
    a11 = input("Your answer (a/b/c/d): ")
    if a11.lower() == "b":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is b) France\n")
        wrong_answers += "11. France gifted the Statue of Liberty to the USA. You answered: " + a11 + "\n"

    # Question 12
    print("12. Which element has the chemical symbol 'O'?")
    print("a) Oxygen")
    print("b) Gold")
    print("c) Silver")
    print("d) Helium")
    a12 = input("Your answer (a/b/c/d): ")
    if a12.lower() == "a":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is a) Oxygen\n")
        wrong_answers += "12. The symbol 'O' stands for Oxygen. You answered: " + a12 + "\n"

    # Question 13
    print("13. What is the largest continent on Earth?")
    print("a) Africa")
    print("b) Asia")
    print("c) Europe")
    print("d) North America")
    a13 = input("Your answer (a/b/c/d): ")
    if a13.lower() == "b":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is b) Asia\n")
        wrong_answers += "13. The largest continent is Asia. You answered: " + a13 + "\n"

    # Question 14
    print("14. Which language is used to create web pages?")
    print("a) Python")
    print("b) HTML")
    print("c) C++")
    print("d) Java")
    a14 = input("Your answer (a/b/c/d): ")
    if a14.lower() == "b":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is b) HTML\n")
        wrong_answers += "14. Web pages are created with HTML. You answered: " + a14 + "\n"

    # Question 15
    print("15. Who discovered penicillin?")
    print("a) Marie Curie")
    print("b) Alexander Fleming")
    print("c) Isaac Newton")
    print("d) Louis Pasteur")
    a15 = input("Your answer (a/b/c/d): ")
    if a15.lower() == "b":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is b) Alexander Fleming\n")
        wrong_answers += "15. Penicillin was discovered by Alexander Fleming. You answered: " + a15 + "\n"

    # Question 16
    print("16. What is the smallest prime number?")
    print("a) 0")
    print("b) 1")
    print("c) 2")
    print("d) 3")
    a16 = input("Your answer (a/b/c/d): ")
    if a16.lower() == "c":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is c) 2\n")
        wrong_answers += "16. The smallest prime number is 2. You answered: " + a16 + "\n"

    # Question 17
    print("17. Which country is known as the Land of the Rising Sun?")
    print("a) China")
    print("b) Japan")
    print("c) Korea")
    print("d) India")
    a17 = input("Your answer (a/b/c/d): ")
    if a17.lower() == "b":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is b) Japan\n")
        wrong_answers += "17. Japan is called the Land of the Rising Sun. You answered: " + a17 + "\n"

    # Question 18
    print("18. How many sides does a hexagon have?")
    print("a) 5")
    print("b) 6")
    print("c) 7")
    print("d) 8")
    a18 = input("Your answer (a/b/c/d): ")
    if a18.lower() == "b":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is b) 6\n")
        wrong_answers += "18. A hexagon has 6 sides. You answered: " + a18 + "\n"

    # Question 19
    print("19. Who is the author of 'Harry Potter'?")
    print("a) J.K. Rowling")
    print("b) J.R.R. Tolkien")
    print("c) Stephen King")
    print("d) Roald Dahl")
    a19 = input("Your answer (a/b/c/d): ")
    if a19.lower() == "a":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is a) J.K. Rowling\n")
        wrong_answers += "19. Harry Potter author is J.K. Rowling. You answered: " + a19 + "\n"

    # Question 20
    print("20. Which instrument has keys, pedals and strings?")
    print("a) Violin")
    print("b) Flute")
    print("c) Piano")
    print("d) Drum")
    a20 = input("Your answer (a/b/c/d): ")
    if a20.lower() == "c":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is c) Piano\n")
        wrong_answers += "20. The instrument with keys, pedals and strings is the piano. You answered: " + a20 + "\n"

    print("Quiz Finished!\n")
    print("Your final score is:", score, "/ 20\n")

    if wrong_answers:
        print("Questions you got wrong and correct answers:")
        print(wrong_answers)
    else:
        print("Excellent! You got all answers correct!")

    retake = input("\nWould you like to retake the test? (yes/no): ").strip().lower()
    if retake not in ('yes', 'y'):
        print("Thank you for playing the MCQ Quiz App!")
        break
    print("\nRestarting the quiz...\n")