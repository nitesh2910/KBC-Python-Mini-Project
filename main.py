questions = [
    [
        "what is the capital of india", "Gandhinagar", "Jaipur", "Delhi", "lucknow", "none", 3
    ],
    [
        "what is the capital of india", "Gandhinagar", "Jaipur", "Delhi", "lucknow", "none", 3
    ],
    [
        "what is the capital of india", "Gandhinagar", "Jaipur", "Delhi", "lucknow", "none", 3
    ],
    [
        "what is the capital of india", "Gandhinagar", "Jaipur", "Delhi", "lucknow", "none", 3
    ],
    [
        "what is the capital of india", "Gandhinagar", "Jaipur", "Delhi", "lucknow", "none", 3
    ],
    [
        "what is the capital of india", "Gandhinagar", "Jaipur", "Delhi", "lucknow", "none", 3
    ],
    [
        "what is the capital of india", "Gandhinagar", "Jaipur", "Delhi", "lucknow", "none", 3
    ],
    [
        "what is the capital of india", "Gandhinagar", "Jaipur", "Delhi", "lucknow", "none", 3
    ],
    [
        "what is the capital of india", "Gandhinagar", "Jaipur", "Delhi", "lucknow", "none", 3
    ],
    [
        "what is the capital of india", "Gandhinagar", "Jaipur", "Delhi", "lucknow", "none", 3
    ],
    [
        "What is the capital of India", "Gandhinagar", "Jaipur", "Delhi", "lucknow", "none", 3
    ],
]

levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 10000000]

money  = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\n Your Question of Rs {levels[i]}")
    print(f"Q. {question[0]}")
    print(f"a. {question[1]},   b. {question[2]}")
    print(f"c. {question[3]},   d. {question[4]}")
    reply = int(input("Enter your Answer (1-4) or 0 to quit\n"))
    
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"correct answer,You have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("Wrong Answer")
        break
print(f"your take home money is {money}")