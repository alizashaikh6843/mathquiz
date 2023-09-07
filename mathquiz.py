import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    elif operator == '/':
        # Ensure the result is an integer
        num1, num2 = num1 * num2, num2
        answer = num1 // num2
    
    question = f"What is {num1} {operator} {num2}? "
    return question, answer

def main():
    print("Welcome to the Math Quiz Game!")
    num_questions = int(input("How many questions do you want to answer? "))
    
    score = 0
    
    for _ in range(num_questions):
        question, correct_answer = generate_question()
        print(question)
        user_answer = int(input("Your answer: "))
        
        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}\n")
    
    print(f"You answered {score} out of {num_questions} questions correctly.")
    if score == num_questions:
        print("Congratulations! You got a perfect score!")

if __name__ == "__main__":
    main()
