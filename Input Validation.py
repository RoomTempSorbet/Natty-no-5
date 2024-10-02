
number = int(input("How many tests do you have? "))


Test_scores = []


for index in range(number):

    test_scores = int(input(f"Enter Test Score for test {index + 1}: "))


    while test_scores < 0 or test_scores > 100:
        print("Invalid Test Score. Please enter a score between 0 and 100.")
        test_scores = int(input(f"Enter Test Score for test {index + 1}: "))


    Test_scores.append(test_scores)


print( Test_scores)

