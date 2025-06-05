import os
from dotenv import load_dotenv
from question_analyzer import QuestionAnalyzer
from question_generator import QuestionGenerator

load_dotenv()

def main():
    # Load the API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        return

    # Initialize components
    analyzer = QuestionAnalyzer(api_key)
    generator = QuestionGenerator(api_key)

    print("Welcome to the Math Problem Generator!")
    print("Enter a math problem, and I'll generate similar ones with multiple choice answers.")
    print("Type 'quit' to exit.")

    while True:
        # Get input from user
        user_input = input("\nEnter a math problem: ").strip()
        
        if user_input.lower() == 'quit':
            break
            
        if not user_input or len(user_input) < 3:
            print("Please enter a valid math problem (at least 3 characters long).")
            continue

        try:
            # Analyze difficulty
            difficulty = analyzer.analyze_difficulty(user_input)
            print(f"\nAnalyzed difficulty level: {difficulty}")
            print(f"Description: {analyzer.difficulty_levels[difficulty]}")

            # Generate similar questions with multiple choice
            questions = generator.generate_question(difficulty, user_input)
            
            # Present each question one at a time
            for i, (question, answers, correct) in enumerate(questions, 1):
                print(f"\nQuestion {i}:")
                print(question)
                print("\nMultiple Choice Answers:")
                for letter, answer in zip(['A', 'B', 'C', 'D'], answers):
                    print(f"{letter}) {answer}")
                
                # Get user's answer
                while True:
                    user_answer = input("\nEnter your answer (A, B, C, or D): ").strip().upper()
                    if user_answer in ['A', 'B', 'C', 'D']:
                        break
                    print("Sorry, that is not a valid choice. Please enter A, B, C, or D.")
                
                # Check if answer is correct
                user_choice = answers[ord(user_answer) - ord('A')]
                if user_choice == correct:
                    print("Correct! Well done!")
                else:
                    print(f"Sorry, that's incorrect. The correct answer was {correct}.")
                
                # Wait for user to press Enter before next question
                input("\nPress Enter to continue to the next question...")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 